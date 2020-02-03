import os
import requests
from app import app


class WikiFile:
    def __init__(self, title="index", path=None):
        self.title = title
        self.path = path or "{}.md".format(title)

    def get_wiki(self):
        request_url = "{}{}page/{}".format(
            app.config.get('WIKI_SERVER'),
            app.config.get('WIKI_API_PATH'),
            self.path,
        )

        app.logger.debug("Send request to '%s'", request_url)
        response = requests.get(request_url)
        app.logger.debug("Get response from '%s' - %s", request_url, response.status_code)

        if response.status_code != 200:
            return None

        return response.text

    def as_dict(self):
        return {
            'title': self.title,
            'path': self.path,
        }

    @classmethod
    def pages(cls, path):
        request_url = "{}{}pages/{}".format(
            app.config.get('WIKI_SERVER'),
            app.config.get('WIKI_API_PATH'),
            path,
        )

        app.logger.debug("Send request to '%s'", request_url)
        response = requests.get(request_url)
        app.logger.debug("Get response from '%s' - %s", request_url, response.status_code)

        response_data = response.json()
        app.logger.debug(response_data.get('status'))
        if response.status_code != 200 or response_data.get('status') != 'success':
            return

        yield from (cls(**page) for page in response_data.get('pages', []) if page.get('title') != 'index')


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
