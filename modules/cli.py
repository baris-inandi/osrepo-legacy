from modules import select
from modules.search import search
from modules.abort import abort


def os_search(keyword: str):
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

    # get confirmation:
    # [?] This will print out all the available OS entries. Are you sure?
    pass


def download_with_id():
    # TODO:
    # osr install pureos@2.0.0
    # or
    # osr install pureos -> triggers select.select_os_version()

    # TODO: select.confirm_download() should be called here
    pass
