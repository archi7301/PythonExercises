# Task №9. Write a Python program to get n (non-negative integer) copies of the first 2 characters of a given string. Return n copies of the whole string if the length is less than 2 (w3resource №23).


def get_copies(str, n):
    if len(str) < 2:
        return None
    str_sliced = str[0:2] * n

    return str_sliced


print(get_copies('hui', 4))