# Task №15. Write a Python program that computes the greatest common divisor (GCD) of two positive integers (w3resource №31).


def calculate_gcd(first_num, second_num):
    if (first_num == 0) and (second_num == 0):
        return first_num + second_num
    if first_num > second_num:
        first_num = first_num % second_num
        return first_num
    else:
        second_num = second_num % first_num
        return second_num


print(calculate_gcd(first_num=12, second_num=8))