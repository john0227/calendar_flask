from flask import redirect, render_template, request, url_for

from . import app
from .calendar_util import my_calendar

import datetime


@app.get('/')
def index():
    now = datetime.datetime.now()
    this_cal, other_cal = my_calendar.get_calendar(now)
    return render_template('calendar.html', this_cal=this_cal, other_cal=other_cal, current_date=now)

@app.post('/add_schedule')
def add_schedule():
    print(request.form)
    return redirect(url_for('index'))
