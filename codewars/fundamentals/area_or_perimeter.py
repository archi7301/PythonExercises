# Task №2:
# You are given the length and width of a 4-sided polygon. The polygon can either be a rectangle or a square.
# If it is a square, return its area. If it is a rectangle, return its perimeter.


def area_or_perimeter(length, width):
    if length == width:
        return pow(length, 2) or pow(length, 2)
    else:
        return (length + width) * 2


print(area_or_perimeter(length=120, width=120))
