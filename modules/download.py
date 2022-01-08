from os import system


def download(d: dict):
    if not d["browser"]:
        # no browser, regular download
        print()
        print("Starting download...")
        system(f"wget {d['url']}")
    else:
        # open browser
        print()
        # TODO: implement browser handler
        print("Handling with browser: ", d["url"])
