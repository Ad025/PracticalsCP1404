"""Writing for loops"""


def main():
    for i in range(0, 101, 10):
        print(i, end=",")
    print()

    print("")

    for j in range(20, 0, -1):
        print(j, end=",")
    print()

    user_input = int(input("Enter an input"))
    for stars in range(user_input):
        print("*", end="")
    print()

    # needed the cheat sheet for this
    user_input2 = int(input("Enter an input"))
    for k in range(user_input2 + 1):
        print("*" * k)
    print()


main()
