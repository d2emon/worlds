import os
from app import app


def get_wiki(page):
    filename = os.path.join(app.config.get('WIKI_ROOT'), page)
    if not os.path.exists(filename):
        return None

    with open(filename, "r", encoding='utf-8') as file:
        content = file.read()

    return content


def list_wiki(slug):
    path = os.path.join(app.config.get('WIKI_ROOT'), slug)
    for file in os.listdir(path):
        if file == "index.md":
            continue
        if not file.endswith(".md"):
            continue
        yield os.path.splitext(os.path.basename(file))[0]


def wikis(
    title,
    wikipedia=True,
    lurkmore=True,
    posmotreli=True,
    **data,
):
    if wikipedia:
        data['wikipedia'] = "https://ru.wikipedia.org/wiki/{}".format(title)
    if lurkmore:
        data['lurkmore'] = "http://lurkmore.to/{}".format(title)
    if posmotreli:
        data['posmotreli'] = "https://posmotre.li/{}".format(title)
    return data
