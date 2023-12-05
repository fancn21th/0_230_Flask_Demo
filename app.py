from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def hello_world():
    return render_template("index.html", name="Hello, World!")


@app.route("/chinese")
def hello_chinese():
    return "你好，世界！"


@app.route("/name/<name>")
def hello_name(name):
    return f"Hello, {name}!"


# mac
# FLASK_APP=app.py flask run
# FLASK_APP=app.py FLASK_ENV=development flask run


# windows
# $env:FLASK_APP = "app.py"; flask run
# $env:FLASK_APP = "app.py"; $env:FLASK_ENV = "development"; flask run
