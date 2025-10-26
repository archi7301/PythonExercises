# Task №1:
# Create a function with two arguments that will return an array of the first n multiples of x.
# Assume both the given number and the number of times to count will be positive numbers greater than 0.

def array_of_multiples(x, n):
    array = []
    if n < 0 or x < 0:
        return "It is not possible to create an array with negative values!"
    else:
        for i in range(1, n):
            if x % i == 0:
                array.append(i)
        return array


try:
    x = int(input("Enter x: "))
    n = int(input("Enter n: "))

    print(array_of_multiples(x, n))

except Exception as e:
    print(e)