# Task №5. Write a Python program to calculate the number of days between two dates (w3resource: №14).


from datetime import date

def calc_difference_of_days():
    print("Enter the first date:")
    year1 = int(input("Year: "))
    month1 = int(input("Month: "))
    day1 = int(input("Day: "))
    date_one = date(year1, month1, day1)

    print("\nEnter the second date:")
    year2 = int(input("Year: "))
    month2 = int(input("Month: "))
    day2 = int(input("Day: "))
    date_two = date(year2, month2, day2)

    difference = abs((date_two - date_one).days)
    return difference

print("\nDifference:", calc_difference_of_days())
