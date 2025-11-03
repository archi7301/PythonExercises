# Task №8. Write a Python program that checks whether a number is between 100 and 1000 or 2000 (w3resource №17).


def check_num_in_range(num):
    if (num in range(100, 1001)) or (num in range(100, 2001)):
        return f"The number {num} is in range from 100 to 1000 (2000)"
    else:
        return None


num = float(input("Enter your number: "))

print(check_num_in_range(num))