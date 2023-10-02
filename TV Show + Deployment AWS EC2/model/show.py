from config.database import connectToMySQL
from flask import flash


DATABASE = "flask_project"

class Show:
    def __init__(self,data):
        self.id = data['id']
        self.title = data['title']
        self.network = data['network']
        self.release_show = data['release_show']
        self.like_show = data['like_show']
        self.userCreate = data['userCreate']
        self.description = data['description']

    @classmethod
    def create(self, data):
        print(data)
        query = """
            INSERT INTO shows (title,description,network,like_show,release_show,userCreate)
            VALUES (%(title)s,%(description)s,%(network)s,%(like_show)s,%(release_show)s,%(userCreate)s);
        """
        return connectToMySQL(DATABASE).query_db(query,data)

    @classmethod
    def get_by_id(self,data):
        query = "SELECT * FROM shows WHERE id = "+str(int(data))
        results = connectToMySQL(DATABASE).query_db(query)
        return results[0]


    @classmethod
    def get_all(self):
        query = """
            SELECT * FROM shows ; 
        """
        results = connectToMySQL(DATABASE).query_db(query)
        
        return results


    @classmethod
    def update_show(self,data):
        query = "UPDATE shows SET title='"+data["title"]+"' , description='"+data["description"]+"', network='"+data["network"]+"' ,release_show='"+data["release_show"]+"'  WHERE id= "+str(int(data["id"]))
        results = connectToMySQL(DATABASE).query_db(query)

    @classmethod
    def react_up_show(self,data):
        query = "UPDATE shows SET like_show=like_show+1 WHERE id="+str(int(data))
        results = connectToMySQL(DATABASE).query_db(query)

    @classmethod
    def react_down_show(self,data):
        query = "UPDATE shows SET like_show=like_show-1 WHERE id="+str(int(data))
        results = connectToMySQL(DATABASE).query_db(query)


    @classmethod
    def delete_show(self,data):
        query = "DELETE FROM shows WHERE id = "+str(int(data))
        return connectToMySQL(DATABASE).query_db(query)