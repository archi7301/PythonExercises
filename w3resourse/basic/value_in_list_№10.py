# Task №10. Write a Python program that checks whether a specified value is contained within a group of values (w3resource №25).


def value_in_list(value, my_list):
    if value in my_list:
        return True
    else:
        return False


value = float(input("Enter the value: "))

print(value_in_list(my_list=[15, 3, 5, 11, 10], value=value))