from flask import Flask, render_template, flash, redirect, url_for
from app.form import RegisterForm
from app import app, db, bcrypt
from app.models import User

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

@app.route('/home')
def home():
    return "page"
