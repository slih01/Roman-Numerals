units_roman = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
tens_roman = ["X", "XX", "XXX", "XL", "LX", "LXX", "LXXX", "XC"]
hundreds_roman = ["C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
thousands_roman = ["M", "MM", "MMM"]

roman_numeral_column = [thousands_roman, hundreds_roman, tens_roman, units_roman]


def convert(num):
    roman_number = ""
    array = [int(x) for x in str(num)]
    counter = 0
    for i in array:
        if i != 0:
            roman_number += roman_numeral_column[counter][i - 1]
        counter = counter + 1
    print(roman_number)


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
                string_decimal_number = str(decimal_number)
                zero_filled_decimal_number = string_decimal_number.zfill(4)
                convert(zero_filled_decimal_number)
                break


ask_for_number()
again = input("Would you like to convert another number? ").lower()
if again == "Yes":
    print("Yes")
else:
    print("No")
