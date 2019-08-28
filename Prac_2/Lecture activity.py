def main():
    GUESS = 5

    number = int(input("Guess a number between 1 and 10:"))
    while number != GUESS:
        print("invalid")
        number = int(input("Guess a number between 1 and 10:"))
    print("correct")



main()




