# Task №14. Write a Python program that prints out all colors from color_list_1 that are not present in color_list_2 (w3resource №29).


def find_unique_colors(color_list_1: list, color_list_2: list):
    color_set_1 = set(color_list_1)
    color_set_2 = set(color_list_2)

    diff_colors = color_set_1.difference(color_set_2)

    return diff_colors


print(find_unique_colors(color_list_1=["White", "Yellow", "Pink", "Purple", "Gray"],
                         color_list_2=["Black", "Green", "Pink", "White"]))