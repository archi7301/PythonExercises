# Задача №1


number = int(input("Enter your number: "))

if number > 0:
    print("The number is positive")
else:
    print("The number is negative")


# Задача №2


my_string = "We step on that glass, it's in the trash"

print(f"\nString's length: {len(my_string)}")  # 40


# Задача №3


new_string = input("\nEnter your string: ")

print(f"{new_string[-1]}\n")


# Задача №4


my_number = int(input("Enter your number: "))

if my_number % 2 == 0:
    print("The number is odd\n")
else:
    print("The number is even\n")


# Задача №5


first_word = input("Enter your first word: ")
second_word = input("Enter your second word: ")

if first_word[0] == second_word[0]:
    print("The first letters are the same\n")
else:
    print("The first letters are not the same\n")


# Задача №6


my_word = input("Enter your word: ")

if my_word[-1] == 'ь' or my_word[-1] == 'ъ':
    print(f"The penultimate letter is {my_word[-2]}")
else:
    print(f"The last letter is {my_word[-1]}")
