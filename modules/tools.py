import inquirer


def abort(msg: str = "Nothing to do."):
    print(msg)
    quit()


def confirm(msg: str = "Do you want to proceed?", default: bool = True):
    confirmation = inquirer.prompt(
        [inquirer.Confirm("is_confirmed", message=msg, default=default)])
    return confirmation
