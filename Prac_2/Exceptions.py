"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
    - valueError occurs when you put a word or letter into the input instead of a numerical
2. When will a ZeroDivisionError occur?
    - occurs when you try divide any number by 0
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
    - yes, i put parameters in place that assured that the users cant input a value of 0
"""


def main():
    try:
        numerator = int(input("Enter the numerator: "))
        denominator = int(input("Enter the denominator: "))
        while denominator == 0:
            print("invalid input, as noting is divisble by 0")
            denominator = int(input("Enter the denominator: "))
        fraction = numerator / denominator
        print(fraction)
    except ValueError:
        print("Numerator and denominator must be valid numbers!")
    # except ZeroDivisionError:
    #   print("Cannot divide by zero!")
    print("Finished.")


main()
