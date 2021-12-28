import click
import re
from time import time
import string
from difflib import SequenceMatcher as matcher
import yaml


def removeduplicate(list):
    new = []
    for i in list:
        if i not in new:
            new.append(i)
    return new


def search(os_list, keywords_input, success_treshold=0.67):
    start_time = time()
    # initial definitions
    filtered_input = []
    passed_filter = []

    # filter the input
    keywords = keywords_input[len("search ".lower()):].split(",")
    for keyword in keywords:
        proper_keyword = keyword.strip("\'").strip("\"").strip(" ")
        filtered_input.append(proper_keyword)
    print(filtered_input, "\n\n")

    # filter the OSes
    for path in os_list:
        print("os path in operation: \t", path)
        filtered = list(filter(None, re.split(' > ', path)))
        filtered_word_sensitive = re.sub('[' + string.punctuation + ']', '> ',
                                         path).split()
        while ">" in filtered:
            filtered == filtered.remove(">")
        while ">" in filtered_word_sensitive:
            filtered_word_sensitive == filtered_word_sensitive.remove(">")
        print("keywords:\t\t ", filtered)
        print("word sensitive:\t\t ", filtered_word_sensitive)
        print("inputed keywords:\t ", filtered_input)

        # compare the values
        all_filtered = removeduplicate(filtered_word_sensitive + filtered)
        print("----------------------------------------------")
        print("success_treshold = ", success_treshold)
        for item in all_filtered:
            for keyword in filtered_input:
                matchval = round(
                    matcher(None, keyword.lower(), item.lower()).ratio(), 3)
                if matchval >= success_treshold:
                    passed_filter.append(path)
        print("\n\n")

    # finalize
    out = list(removeduplicate(passed_filter))
    if len(out) != 0:
        info, success = str("{} results found in {} seconds".format(
            str(len(out)), str(round(float(time.time() - start_time),
                                     3)))), True
    else:
        info, success = "No search results found", False
    return success, out, info


def initialize():
    with open("osrepo.yaml", "r") as stream:
        loaded_data = yaml.safe_load(stream)
    repo = loaded_data["os"]
    meta = loaded_data["meta"]
    return repo, meta


def index(dictionary, key='link'):
    if key in dictionary:
        yield ""
    for k, v in dictionary.items():
        if isinstance(v, dict):
            for s in index(v, key):
                yield f" > {k}{s}"


@click.command("install")
@click.argument("name")
def main(name):
    click.echo(name)


if __name__ == "__main__":
    # main()
    repo, meta = initialize()
    all_os = index(repo)
    print(search(all_os, "ubuntu"))
