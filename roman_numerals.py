units_roman = ["I","II","III","IV","V","VI","VII","VIII","IX"]
tens_roman = ["X","XX","XXX","XL","LX","LXX","LXXX","XC"]
hundreds_roman = ["C","CC","CCC","CD","D","DC","DCC","DCCC","CM"]
thousands_roman = ["M","MM","MMM"]

roman_number_system = [thousands_roman,hundreds_roman,tens_roman,units_roman]

def romanise (num):
    roman_number = ""
    array = [int(x) for x in str(num)]
    counter = 0
    for i in array:
        if i != 0:
            roman_number += roman_number_system[counter][i-1]
        counter = counter+1
    print(roman_number)



while True:
    try:
        decimal_number = int(input("Please enter a number from 1-3999...."))
    except ValueError:
        print("Sorry, you did not enter a number")
    else:
        if not 3999 >= decimal_number >= 1:
            print("Sorry your number was not within the range")
        else:
            romanise(decimal_number)
            break
