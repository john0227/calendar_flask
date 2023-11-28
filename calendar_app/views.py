from flask import render_template

from . import app
from .calendar_util import my_calendar

import datetime

@app.get('/')
def index():
    return render_template('index.html')

@app.get('/calendar')
def show_calendar():
    now = datetime.datetime.now()
    this_cal, other_cal = my_calendar.get_calendar(now)
    return render_template('calendar.html', this_cal=this_cal, other_cal=other_cal, current_date=now)
