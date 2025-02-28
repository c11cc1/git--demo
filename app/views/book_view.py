from flask import render_template

from app.controllers.book_controller import *
from app import app

@app.route('/')
def loginpage():
    print(1)
    return render_template('login.html')

@app.route('/home')
def show_books_view():
    return show_books


@app.route('/add_book', methods=['POST'])
def add_book_view():
    return Book.add_book()

@app.route('/delete/<int:book_id>', methods=['GET'])
def delete_book_view(book_id):
    return Book.delete_book(book_id)



def render_books_page_view(books_data):
    return render_template('index.html', books=books_data)

def render_book_info_page_view(book_info, image_base64):
    return render_template('bookinfo.html', book_info=book_info, image_base64=image_base64)
