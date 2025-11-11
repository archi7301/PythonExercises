# Task №16. Write a Python program to find the least common multiple (LCM) of two positive integers (w3resource №32).


def calculate_lcm(num_1, num_2, i=2):
    if (num_1 == 0) or (num_2 == 0):
        return f"The numbers must be positive!"

    if (type(num_1) != int) or (type(num_2) != int):
        raise TypeError("The numbers must be 'int' literals!")

    divisors = []
    while True:
        if (num_1 % i == 0) and (num_2 % i == 0):
            divisors.append(i)
        i += 1
        if (i > num_1) or (i > num_2):
            break

    print("Divisors:", ", ".join(str(elem) for elem in divisors))

    lcm = (num_1 * num_2) / divisors[-1]

    return f"\nLCM = {lcm}"


try:
    print(calculate_lcm(336, 360))

except Exception as e:
    print(e)