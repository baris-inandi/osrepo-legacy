from yaml import safe_load as load_yaml


def load_repo():
    # load core repo
    with open("osrepo.yaml", "r") as stream:
        core_repo = load_yaml(stream)
    for key in core_repo["osr"]:
        core_repo["osr"][key]["repo"] = "core"

    # load community repo
    with open("community.yaml", "r") as stream:
        community_repo = load_yaml(stream)
    for key in community_repo["osr"]:
        community_repo["osr"][key]["repo"] = "community"

    return {**community_repo["osr"], **core_repo["osr"]}


repo = load_repo()
