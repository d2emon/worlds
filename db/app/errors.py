from app import app, db
from flask import render_template


@app.errorhandler(404)
def error404(error):
    return render_template('error_404.html'), 404


@app.errorhandler(500)
def error500(error):
    return render_template('error_500.html'), 500
