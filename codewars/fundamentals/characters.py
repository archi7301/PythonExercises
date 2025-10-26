# Task №4
# Your goal is to write a function that removes the first and last characters of a string. You're given one parameter, the original string.
# Important: Your function should handle strings of any length ≥ 2 characters. For strings with exactly 2 characters, return an empty string.


def delete_characters(string):
    if len(string) < 2:
        return None
    elif len(string) == 2:
        return ''
    else:
        list_of_str = list(string)
        del list_of_str[0]
        del list_of_str[-1]

        return ','.join(list_of_str)


string = input("Enter your string: ")

print(delete_characters(string))