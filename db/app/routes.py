from app import app
from flask import flash, render_template, redirect, url_for
import uuid
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
    return render_template(
        'index.html',
        title="Home",
        user=user,
        posts=posts,
    )


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash("Login requested for user {username}, remember_me={remember_me}".format(
            username=form.username.data,
            remember_me=form.remember_me.data,
        ))
        return redirect(url_for('index'))
    return render_template(
        'login.html',
        title="Sign In",
        form=form,
    )
