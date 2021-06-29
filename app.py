from flask import Flask
from flask import render_template
from flask import request
from mlb import check_homer

app = Flask(__name__)

@app.route("/")
def homer():
    homer = check_homer()
    return render_template('index.html', homer = homer)
