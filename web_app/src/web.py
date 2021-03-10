from flask import Flask, render_template
from static.py_core import httpmagic as webread

app = Flask(__name__)


@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello/hello.html', name=name)


@app.route('/')
def heartbeat():
    return "service alive"


@app.route('/search')
def search():
    ratings = ['Red', 'Blue', 'Black', 'Orange']
    return render_template("search/search.html", ratings=ratings)


@app.route('/reports')
def reports():
    info = webread.read_http()
    return info


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/app')
def applic():
    return render_template("app/app.html")
