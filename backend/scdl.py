import yt_dlp
from mutagen.easyid3 import EasyID3
from mutagen.id3 import ID3, APIC
import re
import logging

# Configure the logger
logging.basicConfig(
    level=logging.INFO,  # Set the minimum log level
    format="%(levelname)s - %(message)s",  # Customize the log message format
)

logger = logging.getLogger(__name__)

from config import SCDL_OPTS


class SCDownloader:
    def __init__(self, path):
        self.path = path
        self.scdl_opts = SCDL_OPTS.copy()  # Create a copy to modify for this instance
        yt_dlp.utils.std_headers["User-Agent"] = (
            "facebookexternalhit/1.1 (+http://www.facebook.com/externalhit_uatext.php)"  # set this user agent to enable metadata extraction
        )
        self.title = None
        self.track = None
        self.artist = None
        self.uploader = None
        self.album = "scdl"
        self.genre = "Techno"

    def handleSong(self, url):
        with yt_dlp.YoutubeDL(self.scdl_opts) as scdl:
            info = scdl.extract_info(
                url,
                download=False,
            )
            if info:  # if it was downloaded already, info object is None
                self.downloadSong(scdl, url, info)

    def handlePlaylist(self, url):
        self.scdl_opts["noplaylist"] = False

        with yt_dlp.YoutubeDL(self.scdl_opts) as scdl:
            infoPlaylist = scdl.extract_info(
                url,
                download=False,
            )
            entries = infoPlaylist["entries"]
            logger.info("Playlist ID: %s", infoPlaylist["id"])
            logger.info("Total playlist songs: %s", infoPlaylist["playlist_count"])
            logger.info("Songs to be downloaded: %s", len(entries))
            songCounter = 1
            for entry in entries:
                songURL = entry["url"]
                info = scdl.extract_info(songURL, download=False)
                logger.info("Download Song %s of %s ...", songCounter, len(entries))
                self.downloadSong(scdl, songURL, info)
                songCounter += 1
            logger.info("Successfully downloaded playlist!")

    # handle YT and SC seperately in future - now optimized for SC
    def downloadSong(self, scdl, url, info):
        self.handleMetaData(info)
        scdl.download([url])

    def handleMetaData(self, info):
        def uploaderIsArtist():  # assumption: uploader is artist, if title is just track
            if len(metaData) == 1:
                return True
            return False

        def updateFileName():
            self.scdl_opts["outtmpl"][
                "default"
            ] = f"{self.artist} - {self.track}.%(ext)s"

        def setMetaDataForPostprocessor():
            self.scdl_opts["postprocessor_args"] = [
                "-metadata",
                f"title={self.track}",
                "-metadata",
                f"artist={self.artist}",
                "-metadata",
                f"album={self.album}",  # change to uploader if this is wished
                "-metadata",
                f"genre={self.genre}",
            ]

        self.title = info["title"]
        logger.info("Original title: '%s'", (self.title))
        self.uploader = info["uploader"]
        metaData = self.extractTitleAndArtist()

        if uploaderIsArtist():
            self.artist = info["uploader"]
            self.track = metaData[0]
        else:
            self.artist = metaData[0]
            self.track = metaData[1]

        album = info.get("album", None)
        genre = info.get("genre", None)

        if album:
            self.album = album
        if genre:
            self.genre = genre

        logger.info("Sanitized title: %s - %s", self.artist, self.track)
        updateFileName()
        setMetaDataForPostprocessor()

    """
    Sanitize SC title and extract artist and track.
    Returns [artist, track] or just [track], if title contains no '-'
    """

    def extractTitleAndArtist(self):
        def sanitizeString(string):
            brackets = r"\[.*?\]"
            parentheses = r"(\(.*?\)).(\(.*?\))"
            left_of_slash = r".*\|\s*"  # xxx | <-- delete
            stars = r"\*.*?\*"
            string = re.sub(brackets, "", string)
            string = re.sub(left_of_slash, "", string)
            string = re.sub(stars, "", string)
            if re.match(parentheses, string):
                secondParentheses = re.search(parentheses, string).group(2)
                string = string.replace(secondParentheses, "")
            return string

        def splitAndDeleteWhiteSpaces():
            for part in title.split(
                "-", 1
            ):  # meta[0] = artist, meta[1] = track, len=1 if only track
                metaData.append(
                    part.strip()
                )  # strip() deletes leading and tailing whitespaces

        title = sanitizeString(self.title)
        metaData = []
        splitAndDeleteWhiteSpaces()
        return metaData

    def download(self, url):
        if "playlist" in url or "sets" in url:  # sets (Soundcloud)
            self.handlePlaylist(url)
        else:
            self.handleSong(url)
