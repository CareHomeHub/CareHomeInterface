from flask import Flask, render_template

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
    return "Hello search"


@app.route('/reports')
def reports():
    return "Hello reports"


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/app')
def applic():
    return render_template("app/app.html")
