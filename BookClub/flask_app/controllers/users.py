from flask import render_template, redirect, session, request, flash, url_for
from flask_app import app
from flask_app.models.book import Book
from flask_app.models.user import User
from flask_app.models.favorite import Favorite
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)

#===================Redirecting to the Login page==============================
@app.route('/')
def index():
    return redirect('/log_page')


#===================Redirecting to the Login page==============================
@app.route('/log_page')
def log_page():
    return render_template('login.html')


#===================Redirecting to the Registration page==============================
@app.route('/registration')
def reg_page():
    return render_template('registration.html')


#===================Registration method==============================
@app.route('/register', methods=['POST'])
def register():
    if not User.validate_registration(request.form):
        return redirect('/registration')
    data ={ 
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email'],
        "password": bcrypt.generate_password_hash(request.form['password'])
    }
    session['user_id'] = User.save_user(data)
    return redirect('/books')


#===================Login method==============================
@app.route('/login', methods=['POST'])
def login():
    user = User.get_user_by_email(request.form)
    if not user:
        flash("Email doesn't exist in the Database", "login")
        return redirect('/log_page')
    if not bcrypt.check_password_hash(user.password, request.form['password']):
        flash("Invalid Password", "login")
        return redirect('/log_page')
    session['user_id'] = user.id
    return redirect('books')


#===================The logout method==============================
@app.route('/logout')
def logout():
    session.clear()
    return redirect('/log_page')