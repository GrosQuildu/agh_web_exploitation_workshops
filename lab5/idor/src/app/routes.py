import os

from flask import render_template, flash, redirect, url_for, request
from flask_login import login_user, logout_user, current_user, login_required
from werkzeug.urls import url_parse
from app import app, db
from app.forms import LoginForm, RegistrationForm, PostForm
from app.models import User, Post
from datetime import datetime
from shutil import copyfile
from config import ADMIN_PATH
from urllib.parse import unquote

@app.route('/')
@app.route('/profile')
@app.route('/index')
def index():
    if current_user.is_authenticated:
        user = current_user
    else:
        user = User(username="Traveler")
    posts = Post.query.filter_by(user_id=User.query.filter_by(username="random_user").first().id)
    return render_template('user.html', user=user, posts=posts)


@app.route(ADMIN_PATH)
def admin():
    posts = Post.query.all()
    return render_template('index.html', title='Home', posts=posts)


@app.route('/login/', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('profile'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('profile')
        return redirect(url_for('profile'))
    return render_template('login.html', title='Sign In', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))


@app.route('/register/', methods=['GET', 'POST'])
@login_required
def register():
    if current_user.username == "admin":
        form = RegistrationForm()
        if form.validate_on_submit():
            user = User(username=form.username.data)
            user.set_password(form.password.data)
            db.session.add(user)
            db.session.commit()
            flash('Congratulations, you are now a register user!')
            return redirect(url_for('login'))
        return render_template('register.html', title='Register', form=form)
    else:
        return redirect(url_for('index'))


@app.route('/create', methods=['GET', 'POST'])
@login_required
def create():
    if current_user.username == "admin":
        form = PostForm()
        if form.validate_on_submit():
            post = Post(title=form.title.data, content=form.content.data, author=current_user)
            post.update_slug()
            db.session.add(post)
            db.session.commit()
            flash('Your post is now live!')
            return redirect(url_for('profile'))
        return render_template('create.html', title='Create post', form=form)
    else:
        return redirect(url_for('index'))


@app.route('/<slug>')
def detail(slug):
    post = Post.query.filter_by(slug=slug).first()
    # if not post.user == current_user:
    #     return render_template('detail_error.html')
    return render_template('detail.html', post=post)


@app.route('/setup.py')
def setup():
    easy_post = Post.query.filter_by(title="UNLOCK_EASY_SETUP").first()
    if not easy_post:
        return redirect(url_for('static', filename='tip.txt'))
    else:
        if not easy_post.user.username == 'admin':
            return redirect(url_for('static', filename='tip.txt'))
        else:
            copyfile('./app/setup.py', './app/static/setup.py')
            return redirect(url_for('static', filename='setup.py'))
