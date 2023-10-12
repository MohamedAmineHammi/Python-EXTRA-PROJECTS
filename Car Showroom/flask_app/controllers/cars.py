from flask import render_template,redirect,session,request
from flask_app import app
from flask_app.models.car import Car
from flask_app.models.user import User


@app.route('/new')
def new():
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id":session['user_id']
    }
    return render_template('new.html',user=User.get_by_id(data))


@app.route('/create',methods=['POST'])
def create():
    if 'user_id' not in session:
        return redirect('/logout')
    if not Car.validate_car(request.form):
        return redirect('/new')
    data = {
        "user_id": session["user_id"],
        "price": int(request.form["price"]),
        "model": request.form["model"],
        "make": request.form["make"],
        "year": int(request.form["year"]),
        "description": request.form["description"]
    }
    Car.save(data)
    return redirect('/dashboard')

@app.route('/edit/<int:id>')
def edit(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id":id
    }
    user_data = {
        "id":session['user_id']
    }
    edit=Car.get_one(data)
    user=User.get_by_id(user_data)
    return render_template("edit.html",edit=edit,user=user)

@app.route('/update',methods=['POST'])
def update():
    if 'user_id' not in session:
        return redirect('/logout')
    if not Car.validate_car(request.form):
        return redirect('/new')
    Car.update(request.form)
    return redirect('/dashboard')

@app.route('/show/<int:id>')
def show(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id":id
    }
    user_data = {
        "id":session['user_id']
    }
    car=Car.get_one(data)
    print(car)
    user=User.get_by_id(user_data)
    return render_template("show.html",user=user,car=car)

@app.route('/destroy/<int:id>')
def destroy(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id":id
    }
    Car.destroy(data)
    return redirect('/dashboard')