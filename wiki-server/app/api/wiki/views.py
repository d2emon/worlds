from . import blueprint
from app.api.helpers import try_response
from wiki import load_wiki, list_pages


@blueprint.route('/page/<path:page_id>.md', methods=['GET'])
@blueprint.route('/page/<path:path>/<page_id>.md', methods=['GET'])
def get_wiki(page_id='index', path=""):
    try:
        return load_wiki(page_id=page_id, path=path, page_type="page")
    except FileNotFoundError:
        return "Page not found", 404
    except Exception as e:
        return str(e), 500


@blueprint.route('/pages/<path:path>', methods=['GET'])
def get_pages(path):
    return try_response(lambda: {
        'pages': list(list_pages(path)),
    })
