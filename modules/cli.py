import click
from modules import run
from modules.download import download
from modules.update import update as update_repo


@click.command()
def list():
    run.list_all()


@click.command()
@click.argument('query')
def search(query: str):
    download(run.search_os(query))


@click.command()
@click.argument('_id')
def install(_id: str):
    download(run.download_with_id(_id))


@click.command()
def update():
    update_repo()


@click.group(help="CLI tool to manage full development cycle of projects")
def cli():
    pass


commands = [list, search, install, update]

for command in commands:
    cli.add_command(command)
