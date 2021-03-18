import math

def romanise (num):
    if num >=1000:
        print("biggy")

    elif num >=500:
        print("medium")

    elif num >= 100:
        print("Small")
    else:
        print("tiny")


while True:
    try:
        decimal_number = int(input("Please enter a number from 1-3999...."))
    except ValueError:
        print("Sorry, you did not enter a number")
    else:
        if not 3999 >= decimal_number >= 1:
            print("Sorry your number was not within the range")
            decimal_number = int(input("Please enter a number from 1-3999...."))
        else:
            romanise(decimal_number)
            break
