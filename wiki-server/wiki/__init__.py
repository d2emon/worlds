import os
from app import app


def __list_pages(path):
    if not os.path.isdir(path):
        return []
    for file in os.listdir(path):
        if not file.endswith('.md'):
            continue
        # if file == 'index.md':
        #     continue
        yield os.path.splitext(os.path.basename(file))[0]


def __get_wiki(page):
    filename = os.path.join(app.config.get('WIKI_ROOT'), page)

    if not os.path.exists(filename):
        return None

    with open(filename, "r", encoding='utf-8') as file:
        content = file.read()

    return content


def load_wiki(page_id="index", path="", page_type='page'):
    if page_type not in ('page', 'map'):
        return None
    if page_type == 'map':
        path = os.path.join(path, 'map')
    path = os.path.join(path, "{}.md".format(page_id))
    return __get_wiki(path)
