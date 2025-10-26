# Task №3
# This function should test if the factor is a factor of base.
# Return true if it is a factor or false if it is not.


def check_the_factor(base, factor):
    if base % factor == 0:
        return True
    else:
        return False

try:
    base = int(input("Enter the base: "))
    factor = int(input("Enter the factor: "))

    print(check_the_factor(base, factor))

except Exception as e:
    print(e)