from config.database import connectToMySQL
from flask import flash


DATABASE = "flask_project"

class Like:
    def __init__(self,data):
        self.id = data['id']
        self.tv_show = data['tv_show']
        self.user = data['user']
        self.react = data['react']


    @classmethod
    def get_likes(self):
        query = """
            SELECT * FROM likes ; 
        """
        results = connectToMySQL(DATABASE).query_db(query)
        
        return results

    @classmethod
    def add_like(self,data):
        query = """
            INSERT INTO likes (tv_show, user, react)
            VALUES (%(tv_show)s,%(user)s,%(react)s);
        """
        return connectToMySQL(DATABASE).query_db(query,data)

    @classmethod
    def delete_like(self,data):
        query = "DELETE FROM likes WHERE tv_show = '"+str(data)+"'"
        return connectToMySQL(DATABASE).query_db(query)
