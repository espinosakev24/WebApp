from flask import Flask, render_template, flash, redirect, url_for, request
from app.form import RegisterForm
from app.form import LoginForm
from app import app, db, bcrypt
from app.models import User
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.urls import url_parse


@app.route('/register', methods=['GET', 'POST'])
def register():
    registerForm = RegisterForm()
    if registerForm.validate_on_submit():
        print("hello {}".format(registerForm.email.data))
        hashed_password = bcrypt.generate_password_hash(registerForm.password.data).decode('utf-8')
        user = User(username=registerForm.username.data, email=registerForm.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('{} your account has been successfully created!'.format(
            registerForm.username.data))
        return redirect(url_for('home'))
    return render_template('register.html', title = 'Register', form=registerForm)


@app.route('/login', methods=['GET', 'POST'])
def Login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    log = LoginForm()
    if log.validate_on_submit():
        user = User.query.filter_by(username=log.username.data).first()
        if user is None or not bcrypt.check_password_hash(user.password, log.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('home')
        return redirect(next_page)
    return render_template('login.html', title = 'Login', log=log)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/chat')
@login_required
def chat():
    return render_template('chat.html')


@app.route('/home')
@app.route('/')
@login_required
def home():
    return "page"
