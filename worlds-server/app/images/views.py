import requests
# from flask import jsonify, redirect
from app import resize
from . import blueprint


@blueprint.route('/<path:image_url>', methods=['GET'])
def resized(image_url):
    print(image_url)
    url = resize(image_url, '300x300')
    print(url)
    image = requests.get(url)
    # spa = requests.get("{}{}".format(current_app.config['FRONT'], path))
    # return (
    #     spa.content,
    #     spa.status_code,
    #     spa.headers.items()
    # )
    # return redirect(url)
    return (
        image.content,
        image.status_code,
        image.headers.items(),
    )
