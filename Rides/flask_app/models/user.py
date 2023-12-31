from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app import DATABASE
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 


# ================================================User Class that communicates with the users table in the MySQL Database
class User:
    db_name = 'car_pool_schema'
    def __init__(self,db_data):
        self.id = db_data['id']
        self.first_name = db_data['first_name']
        self.last_name = db_data['last_name']
        self.email = db_data['email']
        self.password = db_data['password']
        self.created_at = db_data['created_at']
        self.updated_at = db_data['updated_at']

    @classmethod
    def save(cls,data):
        query = "INSERT INTO users (first_name,last_name,email,password,created_at,updated_at) VALUES(%(first_name)s,%(last_name)s,%(email)s,%(password)s,NOW(),NOW())"
        return connectToMySQL(DATABASE).query_db(query,data)

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL(DATABASE).query_db(query)
        users = []
        for user in results:
            users.append(cls(user))
        return users

    @classmethod
    def get_one(cls,data):
        query = "SELECT * FROM users WHERE id = %(user_id)s;"
        results = connectToMySQL(DATABASE).query_db(query,data)
        if results:  # Check if results exist
            return cls(results[0])  # Return the first dictionary object
        else:
            return None

    @classmethod
    def get_by_email(cls,data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        results = connectToMySQL(DATABASE).query_db(query,data)
        if len(results) < 1:
            return False
        return cls(results[0])

    @staticmethod
    def validate_user(user):
        is_valid = True
        if len(user['first_name']) < 3:
            is_valid = False
            flash("First name must be at least 3 characters.","register")
        if len(user['last_name']) < 3:
            is_valid = False
            flash("Last name must be at least 3 characters.","register")
        if not EMAIL_REGEX.match(user['email']):
            is_valid = False
            flash("Invalid Email Address.","register")
        if len(user['password']) < 8:
            is_valid = False
            flash("Password must be at least 8 characters.","register")
        if not any(char.isdigit() for char in user['password']):
            flash("Password should have at least one numeral","register")
            is_valid= False
        if not any(char.isupper() for char in user['password']):
            flash("Password should have at least one uppercase letter","register")
            is_valid= False
        if user['password'] != user['confirm']:
            is_valid = False
            flash("Passwords do not match!","register")
        return is_valid