from flask import current_app, jsonify


def try_response(f):
    try:
        return jsonify({
            'status': 'success',
            **f(),
        })
    except Exception as e:
        current_app.logger.error(str(e))
        return jsonify({
            'status': 'fail',
            'error': str(e),
        })
