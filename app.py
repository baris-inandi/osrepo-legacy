""" import click
from modules import commands
from modules.download import download
from sys import argv


@click.command("install")
@click.argument("name")
def main(name):
    click.echo(name)


if __name__ == "__main__":
    download(commands.download_with_id(argv[1]))
 """

from modules.cli import cli

cli()
