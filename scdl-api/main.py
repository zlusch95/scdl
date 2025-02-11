from scdl import SCDownloader
from config import DEFAULT_PATH


class Main:
    def __init__(self):
        self.default_path = DEFAULT_PATH

    def run(self):
        url = input("Enter playlist or video URL: ")
        downloader = SCDownloader(self.default_path)
        downloader.download(url)


if __name__ == "__main__":
    Main().run()
