import yaml
import click
from modules.search import search


def load_repo():
    # load core repo
    with open("osrepo.yaml", "r") as stream:
        core_repo = yaml.safe_load(stream)
    for key in core_repo["osr"]:
        core_repo["osr"][key]["repo"] = "core"

    # load community repo
    with open("community.yaml", "r") as stream:
        community_repo = yaml.safe_load(stream)
    for key in community_repo["osr"]:
        community_repo["osr"][key]["repo"] = "community"

    return {**community_repo["osr"], **core_repo["osr"]}


@click.command("install")
@click.argument("name")
def main(name):
    click.echo(name)


if __name__ == "__main__":
    repo = load_repo()
    search(repo, input("OSR >> "))
