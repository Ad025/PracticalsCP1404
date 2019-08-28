def main():
    in_file = open("numbers.txt", "r")
    number1 = int(in_file.readline())
    number2 = int(in_file.readline())
    in_file.close()
    print(number1 + number2)


main()
