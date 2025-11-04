# Task №13. Write a Python program to print all even numbers from a given list of numbers in the same order and stop printing any after 237 in the sequence (w3resource №28).


def get_even_numbers_upto(other_list, limit):
    empty_list = []
    for num in other_list:
        if num > limit:
            return None
        empty_list.append(num)

    for i in empty_list:
        if i % 2 != 0:
            return "There are no even numbers in this list!"
        empty_list.remove(i)



try:
    limit = int(input("Enter the limit to which to search for even numbers: "))

    print(get_even_numbers_upto(other_list=[117, 84, 33, 265, 99, 242, 17, 58, 223, 391], limit=limit))

except Exception as e:
    print(e)