import os
from app import app


def get_wiki(page):
    filename = os.path.join(app.config.get('WIKI_DIR'), page)
    print(filename)
    if not os.path.exists(filename):
        return None

    print('filename')
    with open(filename, "r") as file:
        content = file.read()

    return content
