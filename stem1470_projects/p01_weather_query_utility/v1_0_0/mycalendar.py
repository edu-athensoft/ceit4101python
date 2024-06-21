# mycalendar.py

import datetime

def get_date():
    current_date = datetime.datetime.today()
    return current_date.strftime("%Y-%m-%d")


def get_datetime():
    current_datetime = datetime.datetime.now()
    return current_datetime.strftime("%Y-%m-%d %H:%M:%S")