from flask import Flask

app = Flask(__name__)

# 配置应用程序设置
app.secret_key = 'you-will-never-guess'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

from app.views import login_view,book_view
