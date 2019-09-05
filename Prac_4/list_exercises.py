def main():
    numbers = []
    for i in range(5):
        number = int(input("Number:"))
        numbers.append(number)

    usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface',
                 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer',
                 'bob']
    print("The last number is {}".format(numbers[4]))
    print("the smallest number is {}".format(min(numbers)))
    print("The largest number is {}".format(max(numbers)))
    print("The Average of the numbers is", sum(numbers) / len(numbers))
    username = input("Enter password")
    if username in usernames:
        print("Access granted")

    else:
        print("Access denied")


main()
