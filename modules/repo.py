from yaml import safe_load as load_yaml


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


repo_object = Repo([("community.yaml", "community"), ("osrepo.yaml", "core")])
repo = repo_object.repo
