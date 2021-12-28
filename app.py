import click


@click.command("install")
@click.argument("name")
def search(name):
    click.echo(name)


if __name__ == "__main__":
    search()
