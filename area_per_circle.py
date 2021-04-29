#!/usr/bin/env python3

# Created by: Jonathan Kene
# Created on: Apr. 29, 2021
# This program calculates and displays the area and perimeter of a
# circle with radius 6 cm.

import math


def main():
    print("For a circle that has a radius")
    print("of 6 cm:")
    print("")
    print("Area = {:.2f} cm^2". format(math.pi*6**2))
    print("Perimeter = {:.2f} cm". format(2*math.pi*6))


if __name__ == "__main__":
    main()
