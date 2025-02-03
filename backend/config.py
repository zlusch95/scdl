DEFAULT_PATH = "/Users/tilschulz/Music/dj/scdl_test"

SCDL_OPTS = {
    "paths": {"home": DEFAULT_PATH},
    "download_archive": DEFAULT_PATH + "/" + "history.txt",
    "extract_flat": True,
    "ignoreerrors": True,
    "outtmpl": {"default": "%(uploader)s - %(title)s.%(ext)s"},
    "format": "bestaudio/best",
    "noplaylist": True,
    "writethumbnail": True,
    "restrictfilenames": False,
    "postprocessors": [
        {
            "key": "FFmpegExtractAudio",
            "preferredcodec": "mp3",
            "preferredquality": "320",
        },
        {
            "key": "FFmpegMetadata",
            "add_metadata": True,
        },
        {"key": "EmbedThumbnail"},
    ],
}
