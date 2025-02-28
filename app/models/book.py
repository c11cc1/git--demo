import mysql.connector
from flask import request,jsonify

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="003327",
    database="hhh"
)


class Book:
    @staticmethod
    def get_books(offset):
        cursor = db.cursor(dictionary=True)
        cursor.execute(
            f"SELECT book_id, title, author, publication_date, isbn, category_id, description, price, quantity_available FROM books LIMIT 15 OFFSET {offset}")
        books = cursor.fetchall()
        cursor.close()
        return books


    @staticmethod
    def get_book_by_id(book_id):
        cursor = db.cursor()
        cursor.execute(
            "SELECT book_id, title, author, publication_date, isbn, category_id, description, price, quantity_available FROM books WHERE book_id = %s",
            (book_id,))
        book_info = cursor.fetchone()
        cursor.close()
        return book_info

    @staticmethod
    def show_books():
        # 执行查询
        cursor = db.cursor()
        cursor.execute('SELECT * FROM books')
        books_data = cursor.fetchall()

        # 关闭游标
        # cursor.close()
        # 将查询结果传递给模板进行渲染
        # return render_template('index.html', books=books_data)
        return books_data

    # 添加图书
    @staticmethod
    def add_book(title , author , publication_date , isbn , category_id , description , price , quantity_available , cover):
        cursor = db.cursor()
        cover_data = cover.read()
        insert_query = 'INSERT INTO books (title, author, publication_date, isbn, category_id, description, price, quantity_available, image) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)'
        cursor.execute(insert_query, (title, author, publication_date, isbn, category_id, description, price, quantity_available,cover_data,))
        db.commit()
        cursor.close()
        return 'Book added successfully!'

    # 删除图书功能
    @staticmethod
    def delete_book(book_id):
        cursor = db.cursor()
        cursor.execute('DELETE FROM books WHERE book_id = %s', (book_id,))
        db.commit()
        cursor.close()

