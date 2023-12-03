from flask import redirect, render_template, request, url_for

from . import app
from .calendar_util import my_calendar
from .models import db, Schedule, Task

from collections import defaultdict
import datetime
from typing import Dict, List


cache_start_date: datetime.datetime = None
cache_end_date: datetime.datetime = None
cache_schedules: Dict[int, List[Schedule]] = defaultdict(list)

def cache_db(date: datetime.datetime):
    global cache_start_date, cache_end_date, cache_schedules
    if cache_schedules and cache_start_date <= date <= cache_end_date:
        return
    
    year = date.year
    cache_start_date = datetime.datetime(year=year - 1, month=1, day=1)
    cache_end_date = datetime.datetime(year=year + 1, month=12, day=31)

    start_date = (year - 1) * 10000 + 101  # January 1st of previous year
    end_date = (year + 1) * 10000 + 1231   # December 31st of subsequent year
    schedules: List[Schedule] = Schedule.query.filter(Schedule.date.between(start_date, end_date)).all()

    cache_schedules = defaultdict(list)
    for sch in schedules:
        cache_schedules[sch.date].append(sch)

@app.get('/')
def index():
    this_cal, other_cal = my_calendar.get_calendar(now)
    return render_template('calendar.html', this_cal=this_cal, other_cal=other_cal, current_date=now)
def index(date=None):
    '''
    Displays calendar for the month of given date
    If date is not specified, calendar for today's date is shown
    '''
    if not date:
        date = datetime.datetime.now()
    cache_db(date)

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
