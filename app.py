import click
from modules.search import search
from modules.select_version import select_version


@click.command("install")
@click.argument("name")
def main(name):
    click.echo(name)


if __name__ == "__main__":
    selected, _, _ = search(input("OSR >> "))
    select_version(selected)
