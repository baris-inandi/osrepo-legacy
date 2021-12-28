from time import time
from difflib import SequenceMatcher as matcher
from collections import OrderedDict
from modules.fmt import Fmt


def search(entries: dict[str, dict],
           keyword: str,
           success_treshold=0.65,
           limit=99):
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

    visualize_search(entries, result_list, elapsed)

    return result_list, elapsed


def visualize_search(repo_scope: dict[str, dict], search_result: list[str],
                     elapsed: float):
    for index, entry in enumerate(search_result):
        index += 1
        entry_data = repo_scope[entry]
        # create a repo name string in the following format:
        # number repo/name
        repo_color = "cyan" if entry_data["repo"] == "core" else "red"
        repo_name = Fmt.color('header', str(
            index)) + f" {Fmt.color(repo_color, entry_data['repo'])}/{entry}"
        # generate a repo description in the following format:
        # [from Name Surname] description text comes here
        if entry_data["repo"] == "community":
            added_by = f"{entry_data['added_by']}"
            desc_trail = Fmt.color("green", f"[added by {added_by}] ")
        else:
            desc_trail = ""
        description = f"  {desc_trail}{entry_data['description'][:150]}"
        # number of available versions
        versions_count = len(entry_data["versions"])
        if versions_count > 1:
            versions = Fmt.color("blue",
                                 f" ({versions_count} version(s) available)")
        else:
            versions = Fmt.color("blue",
                                 f" {list(entry_data['versions'].keys())[0]}")
        print(repo_name + versions)
        print(description)
    print(f"search done in {elapsed}s.")
