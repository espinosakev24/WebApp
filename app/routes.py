from flask import Flask, render_template, flash, redirect, url_for
from app.form import RegisterForm
from app import app

@app.route('/register', methods=['GET', 'POST'])
def register():
    registerForm = RegisterForm()
    if registerForm.validate_on_submit():
        flash('Login requested for user {}'.format(
            registerForm.username.data))
        return redirect(url_for('/home'))
    return render_template('register.html', title = 'Register', form=registerForm)

@app.route('/home')
def home():
    return "Home page"
