from app import app
from model.show import Show
from model.user import User
from model.like import Like
from flask import request , redirect, session, render_template, flash
import json





@app.route('/show/create',methods=['post'])
def createShow():
    data = json.loads(request.data)
    Show.create(data)
    return [{"message":"success"}]


@app.route('/show/update',methods=['post'])
def update_show():
    data = json.loads(request.data)
    Show.update_show(data)
    return redirect("/shows")

@app.route('/show/delete/<id>')
def deleteShow(id):
    Show.delete_show(id)
    return redirect("/shows")


@app.route('/shows')
def getAll():
    results = Show.get_all()
    likes = Like.get_likes()

    res = []
    

    for r in results:
        row = {
            "id":r["id"],
            "title":r["title"],
            "date":r["release_show"],
            "network":r["network"],
            "userCreate":r["userCreate"],
            "react":"null"
        }

        res.append(row)

    if(len(likes) > 0):
        for l in likes:
            for r in res:
                if l["user"] == User.userActive and l["tv_show"]==str(r["id"]):
                    r["react"] = "like"


    return render_template('shows.html', data=res,user=User.userActive)


@app.route('/shows/<id>')
def get_by_id(id):
    results = Show.get_by_id(id)
    return render_template('overview.html', data=[results])


@app.route('/react_up/<id>/<user>')
def react_up(id,user):
    results = Show.react_up_show(id)
    results = Like.add_like({"tv_show":id,"user":user,"react":"like"})
    return redirect("/shows")

@app.route('/react_down/<id>')
def react_down(id):
    Show.react_down_show(id)
    Like.delete_like(id)
    return redirect("/shows")

@app.route('/shows/edit/<id>')
def updateShow(id):
    show = Show.get_by_id(id)
    return render_template('update-show.html', data=[show])

@app.route('/shows/new')
def toCreateShow():
    return render_template('create-show.html', user=User.userActive)