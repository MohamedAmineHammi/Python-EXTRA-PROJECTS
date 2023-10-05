from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app import DATABASE

class Book:
    def __init__(self, data_base):
        self.id = data_base['id']
        self.user_id = data_base['user_id']
        self.title = data_base['title']
        self.description = data_base['description']
        self.created_at = data_base['created_at']
        self.updated_at = data_base['updated_at']
    
    #===================Adding a book==============================
    @classmethod
    def add_book(cls, data):
        query = "INSERT INTO books (user_id, title, description) VALUES (%(user_id)s, %(title)s, %(description)s);"
        return connectToMySQL(DATABASE).query_db(query, data)
    
    #===================Getting all books in the DB==============================
    @classmethod
    def get_all_books(cls):
        query = "SELECT * FROM books;"
        results =  connectToMySQL(DATABASE).query_db(query)
        all_books = []
        for row in results:
            all_books.append( row )
        return all_books
    
    #===================Getting one book by id==============================
    @classmethod
    def get_one_book(cls, data):
        query = "SELECT books.id as id, books.user_id as user_id, books.title as title, books.description as description, books.created_at as created_at, books.updated_at as updated_at, users.id as users_id, first_name, last_name FROM books JOIN users ON users.id = books.user_id WHERE books.id = %(book_id)s;"
        results = connectToMySQL(DATABASE).query_db(query, data)
        return results[0]
    
    #===================Updating a book by id==============================
    @classmethod
    def update_book(cls, data):
        query = "UPDATE books SET title=%(title)s, description=%(description)s WHERE id=%(id)s;"
        return connectToMySQL(DATABASE).query_db(query, data)
    
    #===================Delete a book by id==============================
    @classmethod
    def delete_book(cls, data):
        query = "DELETE favorites.*, books.* FROM favorites INNER JOIN books WHERE book_id= books.id and books.id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query, data)
    
    #===================Validate book for creation or updating==============================
    @staticmethod
    def validate_book(book):
        is_valid = True
        if len(book['description']) < 5:
            is_valid = False
            flash("Description must be at least 5 characters","book")
        return is_valid