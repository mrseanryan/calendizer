"""
Generates the model for a calendar month
"""

import date_utils

def get_month_title(month, year):
    return f"{date_utils.month_name(month)} {year}"

def get_column_headers():
    return ['Mon', 'Tue', 'Wed', 'Thurs', 'Fri', 'Sat', 'Sun']

def get_month_data(month, year):
    data = [
        # ['Mon', 'Tue', 'Wed', 'Thurs', 'Fri', 'Sat', 'Sun'],
    ]

    # Generate the calendar data for the month
    days_in_month = date_utils.days_in_month(year, month)

    import pdb
    pdb.set_trace()

    row = None
    for day_of_month in range(1, days_in_month + 1):
        weekday = date_utils.weekday_zero_is_monday(year, month, day_of_month)
        # First row needs fillers:
        if (row == None):
            row = [''] * weekday
        row.append(str(day_of_month))
        if(weekday == 6):
            data.append(row)
            row = []

    if (weekday < 6):
        data.append(row)

    while(len(row) < 7):
        row.append('')

    return data
