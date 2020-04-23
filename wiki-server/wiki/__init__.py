import os
from app import app


def list_pages(path):
    path = os.path.join(app.config.get('WIKI_ROOT'), path)
    if not os.path.isdir(path):
        raise FileNotFoundError("Path not found")

    for file in os.listdir(path):
        if not file.endswith('.md'):
            continue
        # if file == 'index.md':
        #     continue
        yield {
            'title': os.path.splitext(os.path.basename(file))[0],
            'path': os.path.join(path, file),
        }


def __get_wiki(page):
    filename = os.path.join(app.config.get('WIKI_ROOT'), page)

    if not os.path.exists(filename):
        raise FileNotFoundError("Page not found")

    with open(filename, "r", encoding='utf-8') as file:
        content = file.read()

    return content


def load_wiki(page_id="index", path="", page_type='page'):
    if page_type not in ('page', 'map'):
        raise ValueError("Wrong page type")

    if page_type == 'map':
        path = os.path.join(path, 'map')
    path = os.path.join(path, "{}.md".format(page_id))
    return __get_wiki(path)


def list_wiki(slug):
    path = os.path.join(app.config.get('WIKI_ROOT'), slug)
    return list_pages(path)
