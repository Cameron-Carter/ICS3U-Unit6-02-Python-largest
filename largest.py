#!/usr/bin/env python3

# Created by: Cameron Carter
# Created on June 2021
# This program finds the largest of 10 random numbers

import random


def find_largest(numbers):
    # This function determines the largest number
    for counter in range(len(numbers)):
        print("Random number {0} is {1}.".format(
            counter + 1, numbers[counter]
        ))
        if counter == 0:
            largest = numbers[counter]
        else:
            if numbers[counter] > largest:
                largest = numbers[counter]

    return largest


def main():
    # This function generates 10 numbers

    random_numbers = []

    # Process and output
    for loop_counter in range(0, 10):
        generated_number = random.randint(1, 100)
        random_numbers.append(generated_number)
        for loop_counter in range(len(random_numbers)):
            print("Random number {0} is {1}.".format(
                loop_counter + 1, random_numbers[loop_counter]
            ))
    # Call find_largest
    largest_number = find_largest(random_numbers)
    print("\nThe largest number is {}.".format(largest_number))
    print("\nDone.")


if __name__ == "__main__":
    main()
