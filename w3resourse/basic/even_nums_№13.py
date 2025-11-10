# Task №13. Write a Python program to print all even numbers from a given list of numbers in the same order and stop printing any after 237 in the sequence (w3resource №28).


def get_even_numbers_upto(my_list, limit):
    even_numbers = []
    for num in my_list:
        if (num % 2 == 0) and (num < limit):
            even_numbers.append(num)
    return even_numbers


try:
    limit = int(input("Enter the limit: "))
    
    print(get_even_numbers_upto([117, 84, 33, 265, 99, 242, 17, 58, 223, 391], limit))

except Exception as e:
    print()