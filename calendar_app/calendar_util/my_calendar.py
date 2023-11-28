import calendar
import datetime

from typing import List, Tuple

Calendar = List[List[int]]

def get_calendar(date: datetime) -> Tuple[Calendar, Calendar]:
    cal = calendar.monthcalendar(date.year, date.month)
    print(cal)
    for i, week in enumerate(cal):
        for j, day in enumerate(week):
            if day == 0:
                week[j] = -1 if i == 0 else -2
    
    # Get calendar of prev month
    prev_year, prev_month = date.year, date.month - 1
    if prev_month == 0:
        prev_year -= 1
        prev_month = 12
    prev_cal = calendar.monthcalendar(prev_year, prev_month)[-1]

    # Get calendar of next month
    next_year, next_month = date.year, date.month + 1
    if next_month == 13:
        next_year += 1
        next_month = 1
    next_cal = calendar.monthcalendar(next_year, next_month)[0]

    return cal, [prev_cal, next_cal]
