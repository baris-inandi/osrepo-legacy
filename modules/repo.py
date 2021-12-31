from yaml import safe_load as load_yaml
from modules.tools import abort
from modules.entry import Entry
from modules.fmt import Fmt
from modules.tools import confirm


class Repo:
    def __init__(self, repo_files: list[tuple]):
        # example repo_files format:
        # [("osrepo.yaml", "core"), ("community.yaml", "community")]
        sub_repo_list, repo = [], {}
        for file in repo_files:
            sub_repo_list.append(self.parse(*file))
        for sub_repo in sub_repo_list:
            repo.update(sub_repo)
        self.repo = repo

    def parse(self, filename: str, repo_name: str):
        with open(filename, "r") as stream:
            loaded = load_yaml(stream)
        for key in loaded["osr"]:
            loaded["osr"][key]["repo"] = repo_name
        return loaded["osr"]

    def list_all(self):
        # TODO: abort not working
        if confirm(msg="This will print out *ALL* OS entries. Are you sure?"):
            for index, name in enumerate(self.repo.keys()):
                print(Fmt.color("header", str(index + 1)), Entry(name), "\n")
        else:
            abort("Aborted by user.")


repo_object = Repo([("community.yaml", "community"), ("osrepo.yaml", "core")])
repo = repo_object.repo
