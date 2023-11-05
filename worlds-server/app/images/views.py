import requests
from app import resize
from . import blueprint


@blueprint.route('/original/<path:image_url>', methods=['GET'])
def original(image_url):
    image = requests.get(image_url)
    return (
        image.content,
        image.status_code,
        image.headers.items(),
    )


@blueprint.route('/thumb/<path:image_url>', methods=['GET'])
def resized(image_url):
    url = resize(image_url, '300x300')
    image = requests.get(url)
    return (
        image.content,
        image.status_code,
        image.headers.items(),
    )
