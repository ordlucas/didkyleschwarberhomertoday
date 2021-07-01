from flask import Flask
from flask import render_template, make_response, request
from werkzeug.utils import redirect
from mlb import check_homer
from datetime import datetime, timedelta, timezone
import pytz

app = Flask(__name__)

@app.route("/")
def index():
    homer = check_homer()

    # localize timestamp w/ client timezone
    if homer[2] is not None:
        timestamp = datetime.strptime(homer[2], "%Y-%m-%dT%H:%M:%S.%fZ")
        timestamp = pytz.utc.localize(timestamp)
        time_string = timestamp.astimezone(timezone(-timedelta(hours=4))).strftime("%I:%M %p")
    else:
        time_string = None
    
    # render tempalte
    resp = make_response(render_template('index.html', homer = homer[0], opposing_team = homer[1], timestamp = time_string))
    return resp

@app.route("/getOffset", methods = ["GET"])
def getOffset():
    offset = request.args.get("tzOffset")
    resp = make_response("Done")
    resp.set_cookie("tzOffset", offset)
    return resp