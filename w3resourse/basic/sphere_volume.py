# Task №6. Write a Python program to calculate the volume of a sphere with a radius of six (w3resource №15).


import math

def calc_sphere_volume(radius=6):
    volume = (4 * math.pi * pow(radius, 3)) / 3

    return volume


print(calc_sphere_volume())