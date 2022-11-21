#!/usr/bin/env python3

# Created by: Zaida Hammel
# Created on: Nov 2022
# This program adds numbers

import random


def main():
    # this function uses a continue loop
    loop_counter = 0
    answer = 0

    # input
    print("This program adds only positive integers.")
    loop_number = input("Enter the amount of numbers you want to add: ")

    # process
    try:
        int_loops = int(loop_number)
        while loop_counter < int_loops:
            user_str = input("Enter the number you want to add: ")
            int_user = int(user_str)
            if int_user > 0:
                answer = answer + int_user
            else:
                loop_counter = loop_counter + 1
                continue
            loop_counter = loop_counter + 1
        print("The sum is: {0}.".format(answer))
    except ValueError:
        print("Invalid integer")
    finally:
        print("Thanks for playing!")
    # output

    print("\nDone.")


if __name__ == "__main__":
    main()
