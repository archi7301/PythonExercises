# Task №1. Write a Python program that calculates the area of a circle based on the radius entered by the user (w3resource: №4).


import math

def calc_area_circle(radius):
    pi_number = math.pi
    area = pi_number * pow(radius, 2)

    return area


radius = float(input("Enter the radius of the circle: "))

print(calc_area_circle(radius))