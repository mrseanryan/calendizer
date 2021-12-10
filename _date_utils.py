"""
Utils for processing dates.
"""
import calendar

def days_in_month(year, month_index):
    return calendar.monthrange(year, month_index)[1]

# 0 = Mon, 1 = Tue, ...
def weekday_zero_is_monday(year, month, day):
    return calendar.weekday(year, month, day)

def month_name(month):
    return calendar.month_name[month]
