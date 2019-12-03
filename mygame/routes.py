from flask import render_template, flash, redirect, url_for, Flask, request
from mygame import app
from mygame import db
from mygame.forms import LoginForm
from mygame.forms import RegistrationForm
from mygame.models import User
from flask_login import current_user, login_user
from flask_login import logout_user
from flask_login import login_required
from flask import request
from werkzeug.urls import url_parse
from flask_sqlalchemy import SQLAlchemy

"""
routes.py
=============================
program the sets up links to all the other pages on the site
"""

@app.route('/')
@app.route('/homePage')
@app.route('/logout')
def homePage():
    """
    loads the colorPicker as the index page
    """

    return render_template('homePage.html')

@app.route('/color')
@login_required
def index():
    return render_template('colorPicker.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    """
    checks if the user is alredy in the database when they enter their credentials
    """

    if current_user.is_authenticated:
        return redirect(url_for('colorPicker'))

    form = LoginForm()
    if form.validate_on_submit():
        # look at first result first()
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        # return to page before user got asked to login
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')

        return redirect(next_page)
    return render_template('login.html', title='Sign in', form=form)


@app.route('/logout')
def logout():
    """
    allows users to logout when they click the logout button
    """

    logout_user()
    return redirect(url_for('homePage'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    """
    allows users to register a username, it also checks if the username is unique
    """

    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        #user = User(username=form.username.data, email=form.email.data)
        user = User(username=form.username.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route('/orangegame')
def orangegame():
    """
    loads the game with a orange snake body
    """

    return render_template('orangeboard.html')

@app.route('/purplegame')
def purplegame():
    """
    loads the game with a purple snake body
    """

    return render_template('purpleboard.html')

@app.route('/redgame')
def redgame():
    """
    loads the game with a red snake body
    """

    return render_template('redboard.html')

@app.route('/greengame')
def greengame():
    """
    loads the game with a green snake body
    """

    return render_template('greenboard.html')

@app.route('/blackgame')
def blackgame():
    """
    loads the game with a black snake body
    """

    return render_template('blackboard.html')

@app.route('/hardgame')
def hardgame():
    """
    loads the game hard game mode
    """

    return render_template('hardgame.html')

@app.route('/leaderboard')
def leaderboard():
    """
    loads the leaderboard when that button is clicked
    """

    users = User.query.all()
    return render_template('leaderboard.html', title='Leaderboard', users=users)

@app.route('/adminpanel')
def admin():
    """
    loads the admin panel and sends in a list of users and gives the admins the option to clear users
    """

    users = User.query.all()
    return render_template('adminpanel.html', title='Admin Page', users=users)

@app.route('/about')
def about():
    """
    loads the about page with information about the developers
    """

    return render_template('about.html', title='About Page')

@app.route("/adminpanel/", methods=['POST'])
def clearUsers():
    """
    creates the clear users functionality in the admin panel
    """

    users = User.query.all()
    for u in users:
        db.session.delete(u)
        db.session.commit()
    users = User.query.all()
    return render_template('adminpanel.html', title = 'Admin Page', users=users)

@app.route('/postmethod1', methods=['POST'])
def postmethod1():
    """
    this allows user scores for the normal game modes to be saved in the database
    also if the current score is the highest score
    """

    if(current_user.userscore < int(request.form['point'])):
        current_user.userscore=request.form['point']
        db.session.commit()
    users = User.query.all()
    return render_template('leaderboard.html', title = "Leaderboard", users=users)
     # this retrieves the data you passed
     #  request.form['data']

@app.route('/postmethod2', methods=['POST'])
def postmethod2():
    """
    this allows user scores for the game mode with the black snake body to be saved in the database
    also if the current score is the highest score
    """

    if(current_user.blackscore < int(request.form['blackpoint'])):
        current_user.blackscore=request.form['blackpoint']
        db.session.commit()
    users = User.query.all()
    return render_template('leaderboard.html', title = "Leaderboard", users=users)

@app.route('/postmethod3', methods=['POST'])
def postmethod3():
    """
    this allows user scores for the hard game mode to be saved in the database
    also if the current score is the highest score
    """

    if(current_user.hardscore < int(request.form['hardpoint'])):
        current_user.hardscore=request.form['hardpoint']
        db.session.commit()
    users = User.query.all()
    return render_template('leaderboard.html', title = "Leaderboard", users=users)
