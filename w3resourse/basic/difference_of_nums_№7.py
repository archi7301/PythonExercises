# Task №7. Write a Python program to calculate the difference between a given number and 17. If the number is greater than 17, return twice the absolute difference (w3resource №16).


def calc_difference_of_nums(number, const=17):
    if number > const:
        return 2 * (abs(const - number))
    difference = const - number

    return difference


try:
    number = float(input("Enter the number: "))

    print(calc_difference_of_nums(number))

except Exception as e:
    print(e)