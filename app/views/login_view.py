from flask import render_template
from flask import Flask

app = Flask(__name__)
#登录页面
@app.route('/')
def loginpage():
    return render_template('login.html')