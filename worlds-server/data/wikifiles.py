import os
import requests
from app import app


def get_wiki(page):
    request_url = "{}{}{}".format(
        app.config.get('WIKI_SERVER'),
        app.config.get('WIKI_API_PATH'),
        page,
    )

    app.logger.debug("Send request to '%s'", request_url)
    response = requests.get(request_url)
    app.logger.debug("Get response from '%s' - %s", request_url, response.status_code)

    if response.status_code != 200:
        return None

    wiki = response.json()
    if wiki.get('status') != 'success':
        return None
    return wiki.get('wiki')


def list_pages(path):
    if not os.path.isdir(path):
        return []
    for file in os.listdir(path):
        if not file.endswith('.md'):
            continue
        if file == 'index.md':
            continue
        yield os.path.splitext(os.path.basename(file))[0]


def list_wiki(slug):
    path = os.path.join(app.config.get('WIKI_ROOT'), slug)
    return list_pages(path)


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
