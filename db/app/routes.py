import uuid
from app import app, db
from app.models import User
from flask import flash, jsonify, render_template, redirect, request, url_for
from flask_login import current_user, login_user, logout_user, login_required
from flask_wtf.csrf import generate_csrf
from werkzeug.urls import url_parse
from .forms import LoginForm, RegistrationForm


@app.route('/')
@app.route('/index')
@login_required
def index():
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
        posts=posts,
    )


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    form = LoginForm()
    if form.validate_on_submit():
        # flash("Login requested for user {username}, remember_me={remember_me}".format(
        #     username=form.username.data,
        #     remember_me=form.remember_me.data,
        # ))
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))

        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)

    return render_template(
        'login.html',
        title="Sign In",
        form=form,
    )


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(
            username=form.username.data,
            email=form.email.data,
        )
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()

        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))

    return render_template(
        'register.html',
        title="Register",
        form=form,
    )


# API


@app.route('/api')
def api():
    return jsonify({
        'csrf_token': generate_csrf(),
    })


@app.route('/api/index')
@login_required
def api_index():
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
        'csrf_token': generate_csrf(),
        'title': 'Home',
        'messages': [],
        'user': current_user,
        'posts': posts,
    })


@app.route('/api/login', methods=['GET', 'POST'])
def api_login():
    if current_user.is_authenticated:
        return jsonify({'authenticated': True})

    form = LoginForm()
    authenticated = form.validate_on_submit()
    messages = []
    errors = form.errors

    if authenticated:
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            errors['username'] = "Invalid username or password"
            errors['password'] = "Invalid username or password"
        else:
            login_user(user, remember=form.remember_me.data)
            messages.append(
                "Login requested for user {username}, remember_me={remember_me}".format(**form.data)
            )

    return jsonify({
        'authenticated': authenticated,
        'errors': errors,
        'messages': messages,
    })


@app.route('/api/logout')
def api_logout():
    logout_user()
    return jsonify({'authenticated': False})


@app.route('/api/register', methods=['GET', 'POST'])
def api_register():
    if current_user.is_authenticated:
        return jsonify({'registered': False})

    form = RegistrationForm()
    registered = form.validate_on_submit()
    messages = []
    if registered:
        user = User(
            username=form.username.data,
            email=form.email.data,
        )
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()

        messages.append("Congratulations, you are now a registered user!")

    return jsonify({
        'registered': registered,
        'errors': form.errors,
        'messages': messages,
    })
