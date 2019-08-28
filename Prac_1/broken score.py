"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""


def main():
    score = float(input("Enter score: "))
    while score < 0 or score > 100:
        print("Invalid score")
        score = float(input("Enter score: "))

    else:
        if score > 100:
            print("Invalid score")
        elif score >= 90:
            print("Excellent")
        elif score > 50:
            print("Pass")
        else:
            print("Bad")


main()
