from flask import redirect, render_template, request, url_for

from . import app
from .calendar_util import my_calendar
from .models import db, Schedule, Task

import datetime


@app.get('/')
def index():
    now = datetime.datetime.now()
    this_cal, other_cal = my_calendar.get_calendar(now)
    return render_template('calendar.html', this_cal=this_cal, other_cal=other_cal, current_date=now)

@app.post('/add_schedule')
def add_schedule():
    # ImmutableMultiDict([('date', '2023-12-14'), ('schedule_name', 'adfasdf'), ('sch_start', '23:59'), ('sch_end', '23:59')])
    new_sch = Schedule(
        name=request.form['schedule_name'],
        date=int(request.form['date'].replace('-', '')),
        start_time=int(request.form['sch_start'].replace(':', '')),
        end_time=int(request.form['sch_end'].replace(':', ''))
    )
    db.session.add(new_sch)
    db.session.commit()
    return redirect(url_for('index'))
