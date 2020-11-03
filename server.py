"""Server for movie ratings app."""

from flask import Flask
from flask import (Flask, render_template, request, flash, session,
                   redirect)
from model import connect_to_db
import crud
from jinja2 import StrictUndefined

app = Flask(__name__)

app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined

# Replace this with routes and view functions!

@app.route('/')
def homepage():
    """View homepage"""

    return render_template("homepage.html")


@app.route('/movies')
def movie_list():
    """View list of movies"""

    movies= crud.get_movies()

    return render_template('all_movies.html', movies=movies)


@app.route('/movies/<movie_id>')
def show_movie(movie_id):
    """Show details on a particular movie"""

    movie = crud.get_movie_by_id(movie_id)

    return render_template('movie_details.html', movie=movie )

@app.route('/users')
def user_list():
    """View list of users"""

    users = crud.get_users()

    return render_template('users.html', users=users)

@app.route('/users/<user_id>')
def show_user(user_id):
    """Show user profile"""

    user = crud.get_user_by_id(user_id)

    return render_template('user_details.html', user=user)

@app.route('/users', methods=["POST"])
def register_user(): 

    email = request.form.get('email')
    password = request.form.get('password')
    user = crud.get_user_by_email(email)

    if user:
        flash('Email already exists!')
    else:
        crud.create_user(email, password)
        flash('Account created successfully!')

    return redirect('/')

@app.route('/users')
def user_login():

    email = request.form.get('login-email')
    password = request.form.get('login-password')

    user= crud.get_user_by_email(email)
    login_password = crud.get_user_by_password(password)

    session['user'] = User.user_id

    if user:
        flash('Logged in!')

    else:
        flash('Need to create an account!')

    return redirect('/')

if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)

