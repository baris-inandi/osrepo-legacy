import click
from time import time
from difflib import SequenceMatcher as matcher
import yaml
from collections import OrderedDict


def initialize():
    with open("osrepo.yaml", "r") as stream:
        loaded_data = yaml.safe_load(stream)
    repo = loaded_data["os"]
    meta = loaded_data["meta"]
    return repo, meta


def visualize_search(search_result: list, elapsed: float):
    for index, entry in enumerate(search_result):
        index += 1
        print(index, ": ", entry)
    print(f"search done in {elapsed}.")


def search(entries: list, keyword: str, success_treshold=0.67, limit=99):
    time_start = time()
    # parse keywords to a list
    result_dict, result_list = {}, []
    for entry_id in entries:
        match = matcher(None, entry_id.lower(), keyword.lower()).ratio()
        if match >= success_treshold:
            result_dict[match] = entry_id

    # order matching entries
    ordered_index = OrderedDict(sorted(result_dict.items()))
    for i in ordered_index:
        result_list.append(result_dict[i])

    # end time
    time_end = time()
    elapsed = round(time_end - time_start, 2)
    if elapsed == 0:
        elapsed = 0.01

    result_list.reverse()
    result_list = result_list[:limit]

    visualize_search(result_list, elapsed)

    return result_list, elapsed


@click.command("install")
@click.argument("name")
def main(name):
    click.echo(name)


if __name__ == "__main__":
    # main()
    repo, meta = initialize()
    # all_os = index(repo)
    search(repo, input("OSR >> "))

    # print(search(all_os, "ubuntu"))
