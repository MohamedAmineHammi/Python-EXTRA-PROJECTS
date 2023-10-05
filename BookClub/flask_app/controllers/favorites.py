from flask import render_template, redirect, session, request
from flask_app import app
from flask_app.models.favorite import Favorite


#===================Removing a Book from favorites 1==============================
@app.route('/books/unfavorite_showed/<int:id>')
def unfavorite_book_showed(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "book_id": id,
        'user_id': session['user_id']
        
    }
    Favorite.remove_from_favorites(data)
    return redirect(f'/books/{id}')


#===================Removing a Book from favorites 2==============================
@app.route('/books/unfavorite/<int:id>')
def unfavorite_book(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "book_id": id,
        'user_id': session['user_id']
        
    }
    Favorite.remove_from_favorites(data)
    return redirect('/books')


#===================Adding a Book to favorites 1==============================
@app.route('/books/favorite_showed/<int:id>')
def favorite_book_showed(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "book_id": id,
        'user_id': session['user_id']
        
    }
    Favorite.add_to_favorites(data)
    return redirect(f'/books/{id}')


#===================Adding a Book to favorites 2==============================
@app.route('/books/favorite/<int:id>')
def favorite_book(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "book_id": id,
        'user_id': session['user_id']
        
    }
    Favorite.add_to_favorites(data)
    return redirect('/books')
