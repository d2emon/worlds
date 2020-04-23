from flask import jsonify


def try_response(f):
    try:
        return jsonify({
            'status': 'success',
            **f(),
        })
    except Exception as e:
        return jsonify({
            'status': 'fail',
            'error': str(e),
        })
