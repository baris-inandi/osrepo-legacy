from os import system
import webbrowser
from time import sleep
from modules.tools import abort


def download(d: dict):
    if not d["browser"]:
        # no browser, regular download
        print()
        print("Starting download...")
        system(f"wget {d['url']}")
    else:
        # open browser
        print("Continue in browser.")
        sleep(0.1)
        webbrowser.open(d["url"], new=2)
        abort()
