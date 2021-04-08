from flask import Flask, render_template, jsonify
from static.py_core import httpmagic as webread
from flask_cors import CORS
import requests

import logging

# Blueprints
from blueprints.mapper import mapper_blueprint

app = Flask(__name__)
CORS(app)
# setup logger
logger = logging.getLogger('CHH-CORE-API')
logger.setLevel(logging.DEBUG)

# create console handler and set level to debug
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

# create formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# add formatter to ch
ch.setFormatter(formatter)

# add ch to logger
logger.addHandler(ch)

app.register_blueprint(mapper_blueprint)

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    app.logger.info(f"/hello triggered with {name}")
    return render_template('hello/hello.html', name=name)


@app.route('/')
def heartbeat():
    logger.info("/heartbeat triggered")
    return "service alive"


@app.route('/search')
def search():
    logger.info("/search triggered")
    ratings = requests.get("https://carehomehub-platform.herokuapp.com/locations")
    return render_template("search/search.html", ratings=ratings.json())


@app.route('/reports')
def reports():
    logger.info("/reports triggered")
    logger.info("webread.read_http() triggered")
    info = webread.read_http()
    logger.info(f"webread.read_http() returned {info[0]}")
    return jsonify(info)

@app.route('/about')
def about():
    app.logger.info("/about triggered")
    return render_template("about.html")


@app.route('/app')
def applic():
    app.logger.info("/applic triggered")
    return render_template("app/app.html")
