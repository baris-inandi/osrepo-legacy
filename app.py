import click
from modules import cli
from modules.download import download
from sys import argv


@click.command("install")
@click.argument("name")
def main(name):
    click.echo(name)


if __name__ == "__main__":
    download(cli.download_with_id(argv[1]))
