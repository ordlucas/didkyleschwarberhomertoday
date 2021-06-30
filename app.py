from flask import Flask
from flask import render_template, make_response, request
from mlb import check_homer
from datetime import datetime, timedelta, timezone
import pytz

app = Flask(__name__)

@app.route("/")
def index():
    # check if he homered
    homer = check_homer()

    # localize timestamp w/ client timezone
    timestamp = datetime.strptime(homer[2], "%Y-%m-%dT%H:%M:%S.%fZ")
    tz_cookie = request.cookies.get("tzOffset")
    timestamp = pytz.utc.localize(timestamp)
    time_string = timestamp.astimezone(timezone(timedelta(minutes=-int(tz_cookie)))).strftime("%I:%M %p")
    
    # render tempalte
    resp = make_response(render_template('index.html', homer = homer[0], opposing_team = homer[1], timestamp = time_string))
    return resp
