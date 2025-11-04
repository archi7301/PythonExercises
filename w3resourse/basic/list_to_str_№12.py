# Task №12. Write a Python program that concatenates all elements in a list into a string and returns it (w3resource №27).


def convert_list_to_str(my_list):
    string = ''
    for i in my_list:
        string += str(i)

    return string


print(convert_list_to_str([2, 0, 2, 5]))