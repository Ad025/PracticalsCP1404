MIN_LENGHT = 2


def main():
    user_password = input("Please enter a password which has a min of 2 letters:")
    get_password(user_password)


def get_password(user_password):
    while len(user_password) < MIN_LENGHT:
        print("invalid")
        user_password = input("Please enter a password")
    print_password(user_password)


def print_password(user_password):
    for i in range(len(user_password)):
        print("*", end="")


main()
