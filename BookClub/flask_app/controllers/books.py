from flask import render_template, redirect, session, request, flash
from flask_app import app
from flask_app.models.book import Book
from flask_app.models.user import User
from flask_app.models.favorite import Favorite



#===================This method take you to the Book Club page==============================
@app.route('/books')
def books():
    if 'user_id' not in session:
        return redirect('/logout')
    data ={
        'id': session['user_id']
    }
    user = User.get_user_by_id(data)
    books = Book.get_all_books()
    books_list = []
    for book in books:
        check_data = {
            'book_id': book['id'],
            'id': session['user_id'],
            'user_id': session['user_id']
        }
        book_user = User.get_user_by_id(check_data)
        favorite = Favorite.check_favorite(check_data)
        if not favorite:
            favorite = {'book_id' : False}
        books_list.append({'id' : book['id'] , 'title' : book['title'] , 'fname' : book_user.first_name, 'lname' : book_user.last_name, 'favorited': favorite['book_id'] })
    return render_template("club.html", user=user, books=books, books_list=books_list)


# #===================Creating a Book==============================
@app.route('/add_new', methods=['POST'])
def create_book():
    if 'user_id' not in session:
        return redirect('/logout')
    if not Book.validate_book(request.form):
        return redirect('/books')
    data = {
        "user_id": session['user_id'],
        "title": request.form["title"],
        "description": request.form["description"]
    }
    book_id = Book.add_book(data)
    fav_data = {
        "user_id": session['user_id'],
        "book_id": book_id
    }
    Favorite.add_to_favorites(fav_data)
    return redirect('/books')


#===================Showing a Book==============================
@app.route('/books/<int:id>')
def show_book(id):
    if 'user_id' not in session:
        return redirect('/logout')
    book_data = {
        "book_id":id
    }
    user_data = {
        "id":session['user_id']
    }
    book = Book.get_one_book(book_data)
    user = User.get_user_by_id(user_data)
    favorited_users = Favorite.get_all_favorites_for_book(book_data)
    return render_template("creator.html", book=book, user=user, fav_users=favorited_users)


#===================Updating a Book==============================
@app.route('/books/update/<int:id>', methods=['POST'])
def update_book(id):
    if 'user_id' not in session:
        return redirect('/logout')
    if not Book.validate_book(request.form):
        return redirect('/books/<int:id>')
    data = {
        "id": id,
        "title": request.form["title"],
        "description": request.form["description"]
    }
    Book.update_book(data)
    return redirect('/books')


#===================Deleting a Book==============================
@app.route('/books/delete/<int:id>', methods=['POST'])
def delete_book(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id": id
    }
    Book.delete_book(data)
    return redirect('/books')
