from flask import Flask

app = Flask(__name__)

app.secret_key = "thisismysoloproject"

DATABASE = "books_club_schema"