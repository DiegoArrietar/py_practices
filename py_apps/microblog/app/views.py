from flask import render_template, flash, redirect
from app import app
from .forms import LoginForm
from flask_login import login_required, current_user


@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Diego'}
    posts = [
        {
          'author':{'nickname':'John'},
          'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'nickname': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html',title='Home', user=user, posts=posts)


@app.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for email="%s", remember_me=%s'% (form.email.data, str(form.remember_me.data)))
        return redirect('/index')
    return render_template('login.html', title="Sign In", form=form, current_user=current_user)


@app.route('/secret')
@login_required
def secret():
    return 'Only authenticated users are allowed'
