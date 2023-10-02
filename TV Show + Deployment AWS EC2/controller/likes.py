from app import app
from model.like import Like
from flask import request , redirect, session, render_template, flash
import json





@app.route('/likes/add',methods=['post'])
def addLike():
    data = json.loads(request.data)
    Like.add_like(data)
    return [{"message":"success"}]


@app.route('/likes/all')
def getLike():
    results = Like.get_likes()
    return [results]