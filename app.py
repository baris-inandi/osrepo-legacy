import click
from modules.search import search
from modules import select


@click.command("install")
@click.argument("name")
def main(name):
    click.echo(name)


if __name__ == "__main__":
    search_result, elapsed = search(input("OSR >> "))
    if len(search_result) > 0:
        selected_os = select.select_os(search_result, elapsed)
        selected_version = select.select_os_version(selected_os)
        download_url = select.confirm_download(selected_os, selected_version)
    else:
        print("No results found.")
