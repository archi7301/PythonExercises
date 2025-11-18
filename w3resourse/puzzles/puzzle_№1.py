# Task №1. Write a Python program to find a list of integers with exactly two occurrences of nineteen and at least three occurrences of five. Return True otherwise False.
# w3resourse.com puzzle №1


def check_number_of_occurrences():
    numbers = []
    while True:
        number = int(input("Enter the value: "))
        numbers.append(number)
        if len(numbers) > 2:
            ask = input("Do you want to continue? (y/n): ")
            if ask == "n":
                break
        continue

    qty_of_nineteen = numbers.count(19)
    qty_of_five = numbers.count(5)

    if (qty_of_nineteen == 2) and (qty_of_five >= 3):
        return True
    else:
        return False


try:
    print(check_number_of_occurrences())

except Exception as e:
    print(e)