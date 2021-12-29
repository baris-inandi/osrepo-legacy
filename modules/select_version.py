from modules.fmt import format_repo_name, Fmt
from modules.repo import repo
import inquirer


def select_version(entry: str):
    name_fmt = format_repo_name(entry)
    print("\nYou have selected:", name_fmt)
    print("The following versions are available:\n")
    for index, version in enumerate(repo[entry]["versions"]):
        version_fmt = Fmt.underline(Fmt.color('blue', "@" + version))
        version_contributor = ""
        if repo[entry]["repo"] == "community":
            version_contributor = repo[entry]["versions"][version][
                "contributor"]
        print(Fmt.color("header", str(index + 1)), name_fmt + version_fmt,
              Fmt.color("green", f"[added by {version_contributor}]"))

    # TODO: select version here
    selected = "latest"
    print()
    print("selected version", Fmt.color("blue", selected) + ".")

    if repo[entry]["repo"] == "community":
        community_warning()
    Fmt.complain("INFO", "The OS will be downloaded from the following URL:")
    Fmt.complain("INFO",
                 Fmt.underline(repo[entry]["versions"][selected]["url"]))
    # TODO: get [y,n] confirmation here
    print()


def community_warning():
    print()
    Fmt.complain("WARN",
                 "This is a community OS. The download URL is not reviewed.")
    Fmt.complain(
        "WARN", "Make sure you trust the author and check if the URL is safe.")
