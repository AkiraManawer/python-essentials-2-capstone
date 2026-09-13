import platform
import os
import calendar
from datetime import datetime, date


def environment_report():
    file_path = "data/students.txt"

    if os.path.exists(file_path):
        file_size = os.path.getsize(file_path)
        file_status = f"Exists, size: {file_size} bytes"
    else:
        file_status = "Does not exist"

    report = f"""
===== ENVIRONMENT REPORT =====
Operating system: {platform.system()}
Python version: {platform.python_version()}
Working directory: {os.getcwd()}
Student data file: {file_status}
"""

    return report


def date_report():
    today = date.today()
    now = datetime.now()

    future_date = date(2026, 12, 31)
    days_until = (future_date - today).days

    current_year = today.year
    current_month = today.month

    leap_year = calendar.isleap(current_year)
    days_in_month = calendar.monthrange(
        current_year,
        current_month
    )[1]

    report = f"""
===== DATE REPORT =====
Today's date: {today.strftime("%d %B %Y")}
Current timestamp: {now.strftime("%Y-%m-%d %H:%M:%S")}
Days until 31 December 2026: {days_until}
Is the current year a leap year? {leap_year}
Days in the current month: {days_in_month}
"""

    return report
