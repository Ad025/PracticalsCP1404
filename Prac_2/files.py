def main():
    # answer gets print to the name.txt file
    out_file = open("name.txt", "w")
    name = input("Please enter name:")
    print("{}".format(name), file=out_file)
    out_file.close()

    # read the previous name input in file and print on here
    in_file = open("name.txt", "r")
    name = in_file.read().strip()
    in_file.close()
    print("Your name is {} ".format(name))

    # adding up 2 numbers from the numbers.txt file
    in_file = open("numbers.txt", "r")
    number1 = int(in_file.readline())
    number2 = int(in_file.readline())
    in_file.close()
    print(number1 + number2)

    # sum of all numbers from the totalnumbers.txt file
    in_file = open("totalnumbers.txt", "r")
    total = 0
    for line in in_file:
        number = int(line)
        total += number
    in_file.close()
    print(total)


main()
