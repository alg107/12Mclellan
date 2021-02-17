from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def dashboard(name=None):
    return render_template('dashboard.html')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
