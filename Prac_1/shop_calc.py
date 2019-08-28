def main():
    total = 0
    number_of_items = int(input("Number of items:"))

    while number_of_items <= 0:
        print("invalid entry")
        number_of_items = int(input("Number of items:"))

    for i in range(number_of_items):
        price = float(input("Price of item: $"))
        total += price

    if total > 100:
        discount = total - (100 * 0.10)
        print("Total price for {} items is ${:.2f}".format(number_of_items, discount))


    else:
        print("Total price for {} items is ${:.2f}".format(number_of_items, total))


main()
