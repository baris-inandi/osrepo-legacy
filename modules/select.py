from modules.entry import Entry
from modules.fmt import Fmt
import inquirer


def select_os(search_result: list[str], elapsed: float):
    entries = []
    for index, entry in enumerate(search_result):
        current_entry = Entry(entry)
        entries.append(current_entry)
        print(Fmt.color("header", str(index + 1)), current_entry)
    print(f"search done in {elapsed}s.")
    # get selection information here
    # TODO: input() should be replaced with the user selection
    _x = int(input("select an os: ")) - 1
    return entries[_x]


def select_os_version(entry: Entry):
    print("\nThe following versions are available for", entry.formatted_path())
    version_urls = []
    for index, version in enumerate(entry.versions):
        print(Fmt.color("header", str(index + 1)),
              entry.formatted_version(version))
        version_urls.append(version)
    # get selection information here
    # TODO: input() should be replaced with the user selection
    _x = int(input("select version: ")) - 1
    return version_urls[_x]


def confirm_download(entry: Entry, version: str):
    download_url = entry.versions[version]["url"]
    print()
    print("Selected version:", Fmt.underline(version))

    if entry.is_community:
        print()
        Fmt.complain(
            "WARN",
            "This is a community OS. The download URL may not be reviewed.")
        Fmt.complain(
            "WARN",
            "Make sure you trust the author and check if the URL is safe.")
    Fmt.complain("INFO", "The OS will be downloaded from the following URL:")
    Fmt.complain("INFO", Fmt.underline(download_url))

    confirmation = inquirer.prompt([
        inquirer.Confirm("is_confirmed",
                         message="Do you want to proceed?",
                         default=True)
    ])
    print()

    if not confirmation["is_confirmed"]:
        print("aborted by user.")
    else:
        return download_url
