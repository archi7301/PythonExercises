# Task №11. Write a Python program to create a histogram from a given list of integers (w3resource №26).


def build_histogram(items):
    for i in items:
        print("@" * i)


build_histogram([2, 6, 4, 3])