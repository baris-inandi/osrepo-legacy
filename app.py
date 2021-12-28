import click
from time import time
from difflib import SequenceMatcher as matcher
import yaml


def initialize():
    with open("osrepo.yaml", "r") as stream:
        loaded_data = yaml.safe_load(stream)
    repo = loaded_data["os"]
    meta = loaded_data["meta"]
    return repo, meta


def search(entries: list, keywords: str, success_treshold=0.67):
    time_start = time()
    # parse keywords to a list
    keywords_parsed = ["ubuntu", "Debian", "arçh"]
    for entry_id in entries:
        for keyword in keywords_parsed:
            match = matcher(None, entry_id.lower(), keyword.lower()).ratio()
            if match >= success_treshold:
                print(f"{keyword} is similar to {entry_id}")
    # finish timing
    time_end = time()
    elapsed = round(time_end - time_start, 2)
    if elapsed == 0:
        elapsed = 0.01
    return ["result", "oss", "in", "order"], elapsed


@click.command("install")
@click.argument("name")
def main(name):
    click.echo(name)


if __name__ == "__main__":
    # main()
    repo, meta = initialize()
    # all_os = index(repo)
    print(search(repo, "uwu"))
    # print(search(all_os, "ubuntu"))
