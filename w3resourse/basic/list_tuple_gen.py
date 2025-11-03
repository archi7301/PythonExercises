# Task №2. Write a Python program that accepts a sequence of numbers separated by commas from the user and generates a list and a tuple of these numbers (w3resource: №6).


def generate_list_and_tuple(sequence):
    split_sequence = sequence.split(', ')
    my_list = list(split_sequence)
    my_tuple = tuple(split_sequence)

    return f"{my_list}\n{my_tuple}"


sequence = input("Enter the sequence of the nums: ")

print(generate_list_and_tuple(sequence))