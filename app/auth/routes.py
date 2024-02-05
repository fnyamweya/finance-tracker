# app/auth/routes.py
from flask import render_template, redirect, url_for, flash, request
from . import auth
from app.extensions import db
from .forms import RegistrationForm, LoginForm
from app.models import User
from flask_login import login_user, current_user, logout_user
from werkzeug.security import check_password_hash
import bcrypt

@auth.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))

    form = RegistrationForm()

    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()

        if user:
            flash('Email already exists. Please choose a different one.', 'danger')
        else:
            hashed_password = bcrypt.hashpw(form.password.data.encode('utf-8'), bcrypt.gensalt())
            user = User(username=form.username.data, email=form.email.data, password_hash=hashed_password.decode('utf-8'))
            db.session.add(user)
            db.session.commit()
            flash('Your account has been created! You are now able to log in', 'success')
            return redirect(url_for('auth.login'))

    return render_template('auth/register.html', title='Register', form=form)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))

    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()

        if user and bcrypt.checkpw(form.password.data.encode('utf-8'), user.password_hash.encode('utf-8')):
            login_user(user, remember=form.remember_me.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('main.index'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')

    return render_template('auth/login.html', title='Login', form=form)

@auth.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.index'))
