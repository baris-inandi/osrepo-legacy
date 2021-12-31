from modules import select
from modules.search import search
from modules.tools import abort
from modules.repo import repo
from modules.entry import Entry
from modules.fmt import Fmt
from modules.tools import confirm


def search_os(keyword: str):
    # osr list arch
    # returns the download URL of selected os/version.
    search_result, elapsed = search(keyword)
    if len(search_result) > 0:
        selected_os = select.select_os(search_result, elapsed)
        selected_version = select.select_os_version(selected_os)
        download_url = select.confirm_download(selected_os, selected_version)
    else:
        abort("No results found.")
    return download_url


def list_all():
    # osr list *
    # TODO: abort not working
    if confirm(msg="This will print out *ALL* OS entries. Are you sure?"):
        for index, name in enumerate(repo.keys()):
            print(Fmt.color("header", str(index + 1)), Entry(name), "\n")
    else:
        abort("Aborted by user.")


def download_with_id(os_id: str):
    # TODO:
    # osr install pureos@2.0.0
    # or
    # osr install pureos -> triggers select.select_os_version()

    # TODO: select.confirm_download() should be called here
    os_id = os_id.lower()
    os_id_list = os_id.split("@", 1)
    os_name, os_version = os_id_list[0], os_id_list[1]
    print(repo.lower[os_name]["versions"][os_version])
