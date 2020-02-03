from . import blueprint
from app.api.helpers import try_response
from wiki import load_wiki


@blueprint.route('/page/<path:page_id>.md', methods=['GET'])
@blueprint.route('/page/<path:path>/<page_id>.md', methods=['GET'])
def get_wiki(page_id='index', path=""):
    return try_response(lambda: {
        'wiki': load_wiki(page_id=page_id, path=path, page_type="page"),
    })
