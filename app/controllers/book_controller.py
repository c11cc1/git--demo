from flask import request, jsonify, render_template
from app.models.book import Book


def show_books():
    books_data=Book.show_books()
    # 将查询结果传递给模板进行渲染
    return render_template('index.html', books=books_data)

def add_book():
    if request.method == 'POST':
        # 从表单中获取其他字段数据
        title = request.form['title']
        author = request.form['author']
        publication_date = request.form['publication_date']
        isbn = request.form['isbn']
        category_id = request.form['categoryId']
        description = request.form['description']
        price = request.form['price']
        quantity_available = request.form['quantity_available']
        # 从表单中获取上传的图片文件
        cover = request.files['cover']
        if title and author and publication_date and isbn and category_id and description and price and quantity_available and cover:
            return Book.add_book(title , author , publication_date , isbn , category_id , description , price , quantity_available , cover)
        else:
            return 'Invalid request'

def delete_book(book_id):
    #删除图书
    Book.delete_book(book_id)
    #调用show_books来刷新页面
    return show_books()

# @book_blueprint.route('/get_books', methods=['GET'])
# def get_books():
#     page_number = request.args.get('page')
#     offset = (int(page_number) - 1) * 10
#     books = Book.get_books(offset)
#     return jsonify(books)
#
# @book_blueprint.route('/home')
# def show_books():
#     books_data = Book.get_books(0)
#     return render_template('index.html', books=books_data)
#
# @book_blueprint.route('/book-info/<int:book_id>')
# def get_book_info_by_id(book_id):
#     book_info = Book.get_book_by_id(book_id)
#     if book_info:
#         book_info_dict = {
#             'book_id': book_info[0],
#             'title': book_info[1],
#             'author': book_info[2],
#             'publication_date': book_info[3],
#             'isbn': book_info[4],
#             'category_id': book_info[5],
#             'description': book_info[6],
#             'price': book_info[7],
#             'quantity_available': book_info[8]
#         }
#         image_data = get_image_from_database(book_id)
#         if image_data is not None:
#             image_base64 = base64.b64encode(image_data).decode('utf-8')
#             return render_template('bookinfo.html', book_info=book_info_dict, image_base64=image_base64)
#     return render_template('bookinfo.html', book_info=book_info_dict, image_base64=None)
