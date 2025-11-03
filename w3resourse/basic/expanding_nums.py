# Task №3. Write a Python program that takes an integer (n) and calculates the value n+nn+nnn (w3resource: №10).


def expanding_the_numbers(num):
    num_second = num * 2
    num_third = num * 3
    sum = int(num) + int(num_second) + int(num_third)

    return sum


num = input("Enter your num: ")

print(expanding_the_numbers(num))