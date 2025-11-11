# Task №15. Write a Python program that computes the greatest common divisor (GCD) of two positive integers (w3resource №31).


def calculate_gcd(first_num, second_num, i=2):
    if (first_num < 0) or (second_num < 0):
        return "The number must be positive!"
    if (not isinstance(first_num, int)) or (not isinstance(second_num, int)):
        raise TypeError("The number must represent the 'int' type.")

    gcd_list = []
    while True:
        if (first_num % i == 0) and (second_num % i == 0):
            gcd_list.append(i)
        i += 1
        if (i > first_num) or (i > second_num):
            break

    return f"gcd = {gcd_list[-1]}"

try:
    print(calculate_gcd(18, 12))

except Exception as e:
    print(e)