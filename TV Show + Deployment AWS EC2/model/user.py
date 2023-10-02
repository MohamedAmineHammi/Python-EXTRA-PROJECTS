from config.database import connectToMySQL
from flask import flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

DATABASE = "flask_project"

class User:
    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.userActive = None


    @classmethod
    def create_user(cls, data):
        query = """
            INSERT INTO users (first_name, last_name, password, email)
            VALUES (%(first_name)s,%(last_name)s,%(password)s,%(email)s);
        """
        return connectToMySQL(DATABASE).query_db(query,data)
    

    @classmethod
    def get_by_email(cls,data):
        query = "SELECT * FROM users WHERE email = '"+str(data)+"'"
        results = connectToMySQL(DATABASE).query_db(query)
        
        return results[0]

    @classmethod
    def check_email(cls,data):
        query = "SELECT * FROM users WHERE email = '"+str(data)+"'"
        results = connectToMySQL(DATABASE).query_db(query)
        
        return results


    @classmethod
    def get_by_id(cls,data):
        query = """
            SELECT * FROM users WHERE id = %(id)s; 
        """
        results = connectToMySQL(DATABASE).query_db(query,data)
        if len(results)<1:
            return False
        return cls(results[0])