# Task №4. Write a Python program that outputs a calendar for a given month and year (w3resource: №12).


import calendar

def display_the_calendar(year, month):
    if (not isinstance(year, int)) or (not isinstance(month, int)):
        raise TypeError("The entered year and month must match the type 'int'!")

    my_calendar = calendar.month(year, month)

    return my_calendar


try:
    year = int(input("Enter the year: "))
    month = int(input("Enter the month: "))

    print(display_the_calendar(year, month))

except Exception as e:
    print(e)