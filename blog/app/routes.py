import requests
import uuid
from app import app
from flask import jsonify, request
from .forms import LoginForm


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'd2emon'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!',
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!',
        },
        {
            'author': {'username': 'Hippolite'},
            'body': 'People=shit!',
        },
        {
            'id': uuid.uuid4(),
            'slug': 'post-1',
            'author': {
                'firstName': 'First',
                'lastName': 'Last',
            },
            'title': 'Post 1',
            'date': '01 May 2017',
            'summary': 'Post 1',
            'body': 'Post',
            'image': 'https://image.ibb.co/bF9iO5/1.jpg',
        },
        {
            'id': uuid.uuid4(),
            'slug': 'post-2',
            'author': {
                'firstName': 'First',
                'lastName': 'Last',
            },
            'title': 'Post 2',
            'date': '01 May 2017',
            'summary': 'Post 2',
            'body': 'Post',
            'image': 'https://image.ibb.co/bF9iO5/1.jpg',
        },
        {
            'id': uuid.uuid4(),
            'slug': 'post-3',
            'author': {
                'firstName': 'First',
                'lastName': 'Last',
            },
            'title': 'Post 3',
            'date': '01 May 2017',
            'summary': 'Post 3',
            'body': 'Post',
            'image': 'https://image.ibb.co/bF9iO5/1.jpg',
        },
    ]
    return jsonify({
        'title': "Home",
        'user': user,
        'posts': posts,
    })


@app.route('/login', methods=['POST'])
def login():
    form = LoginForm(request.form)
    form.validate()

    client = requests.session()

    r = client.get('http://db:5000/api')
    csrf_token = r.json().get('csrf_token')

    r = client.post(
        'http://db:5000/api/login',
        data={
            'csrf_token': csrf_token,
            'username': form.username.data,
            'password': form.password.data,
            'remember_me': form.remember_me.data,
        }
    )
    data = r.json()

    authenticated = data.get('authenticated')
    error = data.get('error')

    messages = []
    if authenticated:
        messages.append("Login requested for user {username}, remember_me={remember_me}".format(**form.data))
    if error:
        messages.append(error)

    return jsonify({
        'result':
            (len(form.errors) == 0)
            and "Login requested for user {username}, remember_me={remember_me}".format(**form.data),
        'errors': form.errors,
        'messages': messages,
    })


@app.route('/logout', methods=['POST'])
def logout():
    client = requests.session()
    data = client.get('http://db:5000/api/logout').json()
    return jsonify({'result': True})
