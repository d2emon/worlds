from flask import current_app
import requests
from ..database import connect
from ..exceptions import StopGame


class Model:
    database_name = "DATABASE"

    def __init__(self, **kwargs):
        pass

    @classmethod
    def database(cls):
        return connect(cls.database_name)

    @classmethod
    def all(cls):
        return (cls(**data) for data in cls.database().all() if data is not None)

    @classmethod
    def get(cls, item_id):
        data = cls.database().get(item_id)()
        return cls(**data) if data is not None else None

    @classmethod
    def filters(cls, **kwargs):
        return []

    @classmethod
    def find(cls, items=None, **kwargs):
        if items is None:
            items = cls.all()
        filters = list(cls.filters(**kwargs))
        return (item for item in items if all(item and f(item) for f in filters))


class RequestModel:
    _url = "http://worlds_walker_1:5000/api"

    @classmethod
    def _log_request(cls, url, request):
        response = request()
        current_app.logger.debug("Response from '%s' - %s", url, response.status_code)
        try:
            data = response.json()
        except:
            current_app.logger.debug(response.content)
            raise StopGame("Unknown exception: {}".format(response.status_code))
        current_app.logger.debug(data)
        if response.status_code == 404:
            return {}
        if response.status_code != 200:
            raise StopGame(data.get('error', "Unknown exception: {}".format(response.status_code)))
        return data

    @classmethod
    def _parse_response(cls, data):
        return data.get('character')

    @classmethod
    def _post(cls, url, json):
        current_app.logger.debug("POST %s: %s", url, json)
        data = cls._log_request(url, lambda: requests.post(url, json=json))
        return cls._parse_response(data)

    @classmethod
    def _get(cls, url):
        current_app.logger.debug("GET %s", url)
        data = cls._log_request(url, lambda: requests.get(url))
        return cls._parse_response(data)

    @classmethod
    def _put(cls, url, values):
        current_app.logger.debug("PUT %s: %s", url, values)
        data = cls._log_request(url, lambda: requests.put(url, values))
        return cls._parse_response(data)

    @classmethod
    def _delete(cls, url):
        current_app.logger.debug("DELETE %s", url)
        data = cls._log_request(url, lambda: requests.delete(url))
        return data.get('result')
