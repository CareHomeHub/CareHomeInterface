from flask import Flask, render_template, jsonify
from static.py_core import httpmagic as webread
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    app.logger.info(f"/hello triggered with {name}")
    return render_template('hello/hello.html', name=name)


@app.route('/')
def heartbeat():
    app.logger.info("/heartbeat triggered")
    return "service alive"


@app.route('/search')
def search():
    app.logger.info("/search triggered")
    ratings = ['Red', 'Blue', 'Black', 'Orange']
    return render_template("search/search.html", ratings=ratings)


@app.route('/reports')
def reports():
    app.logger.info("/reports triggered")
    info = webread.read_http()
    app.logger.info("webread.read_http() triggered")
    app.logger.info(f"webread.read_http() returned {info[0]}")
    return jsonify(info)


@app.route('/about')
def about():
    app.logger.info("/about triggered")
    return render_template("about.html")


@app.route('/app')
def applic():
    app.logger.info("/applic triggered")
    return render_template("app/app.html")
