from flask import Flask , render_template , url_for ,request
from controller import users , shows ,likes
from app import app


if __name__ =='__main__':
    app.run(debug=True, port=7000)