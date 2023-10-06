from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app import DATABASE

class Favorite:
    def __init__(self, data_base):
        self.id = data_base['id']
        self.user_id = data_base['user_id']
        self.book_id = data_base['book_id']
        self.created_at = data_base['created_at']
        self.updated_at = data_base['updated_at']
    
    
    #===================Add a book to favorites==============================
    @classmethod
    def add_to_favorites(cls, data):
        query = "INSERT INTO favorites (user_id, book_id) VALUES (%(user_id)s, %(book_id)s);"
        return connectToMySQL(DATABASE).query_db(query, data)
    
    
    #===================Remove a book from favorited list==============================
    @classmethod
    def remove_from_favorites(cls, data):
        query = "DELETE FROM favorites WHERE user_id = %(user_id)s AND book_id = %(book_id)s;"
        return connectToMySQL(DATABASE).query_db(query, data)
    
    
    #===================Get all users who favorited the book by it's id==============================
    @classmethod
    def get_total_favorited(cls, data):
        query = "SELECT id, first_name, last_name FROM users JOIN favorites ON users.id = user_id JOIN books ON favorites.book_id = books.id WHERE books.id = %(book_id)s;"
        return connectToMySQL(DATABASE).query_db(query, data)
    
    
    #===================Get all the items in favorites table==============================
    @classmethod
    def get_all_favorites(cls):
        query = "SELECT * FROM favorites;"
        results = connectToMySQL(DATABASE).query_db(query)
        return results
    
    
    #===================Get users who favorites a certain book==============================
    @classmethod
    def get_all_favorites_for_book(cls, data):
        query = "SELECT favorites.user_id as fav_user_id, favorites.book_id as fav_book_id, books.id as books_id, books.title as books_title, books.user_id as books_user_id, users.id as users_id, users.first_name, users.last_name FROM favorites JOIN users ON favorites.user_id = users.id JOIN books ON books.id = favorites.book_id WHERE book_id = %(book_id)s;"
        results = connectToMySQL(DATABASE).query_db(query, data)
        return results
    
    
        #===================Check if the User already favorites the Book==============================
    @classmethod
    def check_favorite(cls, data):
        query = "SELECT book_id FROM favorites WHERE user_id = %(user_id)s AND book_id = %(book_id)s;"
        result = connectToMySQL(DATABASE).query_db(query, data)
        if result:
            return result[0]
        else:
            return None

