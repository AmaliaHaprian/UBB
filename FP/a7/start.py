from jproperties import Properties
from src.ui.ui import *
from src.tests.tests import Test
def get_repo_from_properties():
    configs=Properties()
    with open("settings.properties", 'rb') as config_file:
        configs.load(config_file)
    repo_string=configs.get("repo").data
    repo=""
    if repo_string=="Memory":
        repo=MemoryRepo()
    elif repo_string == "Text":
        repo = TextRepo()
    elif repo_string == "Binary":
        repo = BinaryRepo()
    return repo

ui=UI(get_repo_from_properties())
ui.start()
