import os
from app import app


def get_wiki(page):
    filename = os.path.join(app.config.get('WIKI_ROOT'), page)
    if not os.path.exists(filename):
        return None

    with open(filename, "r") as file:
        content = file.read()

    return content
