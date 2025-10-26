# Task №5
# Write a program that finds the summation of every number from 1 to num (both inclusive).
# The number will always be a positive integer greater than 0.


def summation(num):
    summation_tist = []
    if num < 0:
        return f"The number {num} is not postive"
    else:
        for i in range(1, num + 1):
            summation_tist.append(i)

        return sum(summation_tist)


try:
    num = int(input("Enter the num: "))

    print(summation(num))

except Exception as e:
    print(e)
