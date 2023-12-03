from ..models import Schedule, Task

import calendar as cld
import datetime
from typing import Dict, List, Tuple


class CalendarDate:
    def __init__(self, year: int, month: int, day: int, schedules: List[Schedule], in_view: bool) -> None:
        self.year = year
        self.month = month
        self.day = day
        self.date_str = f'{self.year}-{str(self.month).zfill(2)}-{str(self.day).zfill(2)}'
        self.schedules = schedules
        self.schedules.sort(key=lambda s: len(s.name))
        self.in_view = in_view
    
    def __repr__(self) -> str:
        return f'{self.year}.{self.month}.{self.day} [{self.in_view}]'


class Calendar:
    Dates = List[List[Tuple[int, int, int]]]  # List[List[(year, month, day)]]

    def __init__(self, calendar: List[List[CalendarDate]]) -> None:
        self.calendar = calendar
    
    def __iter__(self):
        return iter(self.calendar)

    @staticmethod
    def get_dates(date: datetime.datetime) -> Dates:
        # Get calendar of prev month
        prev_year, prev_month = date.year, date.month - 1
        if prev_month == 0:
            prev_year -= 1
            prev_month = 12
        prev_cal = cld.monthcalendar(prev_year, prev_month)[-1]

        # Get calendar of next month
        next_year, next_month = date.year, date.month + 1
        if next_month == 13:
            next_year += 1
            next_month = 1
        next_cal = cld.monthcalendar(next_year, next_month)[0]

        cal = cld.monthcalendar(date.year, date.month)
        for i, week in enumerate(cal):
            for j, day in enumerate(week):
                if day == 0:  # if day is not part of current month
                    if i == 0:  # if day is in first week
                        week[j] = (prev_year, prev_month, prev_cal[j])
                    else:  # by def, day is in last week
                        week[j] = (next_year, next_month, next_cal[j])
                else:
                    week[j] = (date.year, date.month, day)
        return cal

    @classmethod
    def build(cls, date: datetime.datetime, schedules: Dict[int, List[Schedule]]) -> 'Calendar':
        def build_key(year: int, month: int, day: int) -> int:
            return year * 10000 + month * 100 + day
        
        dates = cls.get_dates(date)
        calendar = []
        for week in dates:
            cal_week = []
            for dd in week:
                y, m, d = dd
                db_key = build_key(y, m, d)
                cdate = CalendarDate(y, m, d, schedules.get(db_key, []), m == date.month)
                cal_week.append(cdate)
            calendar.append(cal_week)

        return Calendar(calendar)


def get_calendar(date: datetime, schedules: Dict[int, Schedule]) -> Calendar:
    return Calendar.build(date, schedules)
