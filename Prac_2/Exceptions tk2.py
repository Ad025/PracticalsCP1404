"""
   CP1404/CP5632 - Practical
   Fill in the TODOs to complete the task
   """


def main():
    result = 0
    finished = False
    while not finished:
        try:
            result = int(input("Please enter a number: "))
            finished = True
        except ValueError:
            print("Please enter a valid integer.")

    print("Valid result is:", result)


main()
