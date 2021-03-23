units_roman = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
tens_roman = ["X", "XX", "XXX", "XL", "LX", "LXX", "LXXX", "XC"]
hundreds_roman = ["C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
thousands_roman = ["M", "MM", "MMM"]

roman_numeral_column = [thousands_roman, hundreds_roman, tens_roman, units_roman]


# Function Convert number between 1-3999 to Roman Numeral:

def convert(num):
    roman_number = ""
    array = [int(x) for x in str(num)]
    counter = 0
    for i in array:
        if i != 0:
            roman_number += roman_numeral_column[counter][i - 1]
        counter = counter + 1
    print(roman_number)


# Function obtains valid number and converts it to 4-digit number to include leading zeros:

def ask_for_number():
    while True:
        try:
            decimal_number = int(input("Please enter a number from 1-3999...."))
        except ValueError:
            print("Sorry, you did not enter a number")
        else:
            if not 3999 >= decimal_number >= 1:
                print("Sorry your number was not within the range")
            else:
                # Convert number to 4 digit number ie 123 will be 0123
                string_decimal_number = str(decimal_number)
                zero_filled_decimal_number = string_decimal_number.zfill(4)
                convert(zero_filled_decimal_number)
                break


while True:
    try:
        ask_for_number()
        again = str(input("Would you like to convert another number? Enter ""'yes' "" ").lower())
    except TypeError:
        print("Sorry wrong entry")
    else:
        if again == "yes":
            continue
        else:
            print("Ok, programme ending")
            break
