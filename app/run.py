from flask import Flask

from flask import render_template

from app import app

if __name__ == '__main__':
    app.run(host='127.0.0.1', debug=True, port=3398)

