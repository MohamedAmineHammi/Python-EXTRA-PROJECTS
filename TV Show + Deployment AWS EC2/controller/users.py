from app import app
from model.user import User
from flask import request , redirect, session, render_template, flash
from flask_bcrypt import Bcrypt
import json


bcrypt = Bcrypt(app)

app.secret_key = 'project_amine_hammi'

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/register',methods=['post'])
def register():
    data = json.loads(request.data)
    hashed_password = bcrypt.generate_password_hash(data['password'])
    data["password"] = hashed_password
    session['user_id'] = User.create_user(data)
    return [{"message":"success"}]


@app.route('/login',methods=['post'])
def login():
    try:
        data = json.loads(request.data)
        result = User.get_by_email(data["email"])
        if not bcrypt.check_password_hash(result["password"], data['password']):
            return [{"message":"password incorrect"}]
        else:
            User.userActive = result["first_name"]+" "+result["last_name"]
            return [result]
    except Exception as e:
        return [{"message":"email invalid"}]   

@app.route('/check-user',methods=['post'])
def checkEmail():
    try:
        data = json.loads(request.data)
        result = User.check_email(data["email"])
        if(len(result) > 0):
            return [{"message":"exist"}]
        else:
            return [{"message":"not exist"}]

    except Exception as e:
        print(e)       



@app.route('/logout')
def logout():
    session.clear()
    return redirect("/")















