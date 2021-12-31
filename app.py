import click
from modules import cli


@click.command("install")
@click.argument("name")
def main(name):
    click.echo(name)


if __name__ == "__main__":
    cli.download_with_id(input("> "))
