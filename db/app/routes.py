import uuid
from app import app, db
from app.models import User
from flask import flash, render_template, redirect, request, url_for
from flask_login import current_user, login_user, logout_user, login_required
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
