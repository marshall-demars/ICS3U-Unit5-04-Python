#!/usr/bin/env python3

# Created by: Marshall Demars
# Created on: Dec 2022
# This program finds the volume of a cylinder

import math


def cylinder_volume_calculation(radius, height):
    # This function calculates the volume of the cylinder

    # Process
    if radius < 0 or height < 0:
        return -1
    else:
        volume = math.pi * radius**2 * height

    return volume


def main():
    # This function gets the inputs and does try catch

    # Input
    radius_as_string = input("Enter the radius of the cylinder (cm): ")
    height_as_string = input("Enter the height of the cylinder (cm): ")

    try:
        radius_as_int = int(radius_as_string)
        height_as_int = int(height_as_string)
        # Call function
        volume = cylinder_volume_calculation(radius_as_int, height_as_int)
        if volume == -1:
            print("\nPlease input a positive number.")
        else:
            print(
                "\nThe volume of a cylinder with the radius of {0} cm and the height of {1} cm is {2} cm³.".format(
                    radius_as_int, height_as_int, volume
                )
            )
    except Exception:
        print("\nInvalid Input.")

    print("\nDone.")


if __name__ == "__main__":
    main()
