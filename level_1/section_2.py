# Задача №1


while True:
    try:
        my_num = int(input("Enter your number: "))
        break
    except ValueError:
        print("Error: You must enter an integer!")

num_str = str(my_num)

print(f"The first digit of a number is {num_str[0]}\n")


# Задача №2


while True:
    try:
        my_num = int(input("Enter your number: "))
        break
    except ValueError:
        print("Error: You must enter an integer!")

num_str = str(my_num)

print(f"The last digit of a number is {num_str[-1]}\n")


# Задача №3


while True:
    try:
        new_num = int(input("Enter your num: "))
        break
    except ValueError:
        print("Error: You must enter an integer!")

num_str = str(new_num)

first_num = int(num_str[0])
second_num = int(num_str[-1])

print(f"The sum of the first and last digits of a number is {first_num + second_num}\n")


# Задача №4


while True:
    try:
        number = int(input("Enter the number: "))
        break
    except ValueError:
        print("Error: You must enter an integer!")

str_num = str(number)

print(f"The number of digits in this number is {len(str_num)}\n")


# Задача №5


while True:
    try:
        first_number = int(input("Enter your first number: "))
        second_number = int(input("Enter your second number: "))
        break
    except ValueError:
        print("Error: You must enter an integer!")

first_num_str = str(first_number)
second_num_str = str(second_number)

if first_num_str[0] == second_num_str[0]:
    print("The first digits of these numbers are the same\n")
else:
    print("The first digits of these numbers are not the same\n")


# Задача №6


my_list = [1, 2, 3, 4, 5, 6]

print(f"Original list: {my_list}")

for nums in my_list[3:]:
    my_list.pop()

print(f"The new popped list: {my_list}")
