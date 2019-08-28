"""
updated program so that it prints the output to a text file
"""
import random

MAX_INCREASE = 0.175  # 17.5%
MAX_DECREASE = 0.05  # 5%
MIN_PRICE = 1
MAX_PRICE = 100
INITIAL_PRICE = 10.0


def main():

    out_file = open("output.txt", "w")

    price = INITIAL_PRICE
    day = 0
    print("Starting price: ${:,.2f}".format(price), file=out_file)

    while MIN_PRICE <= price <= MAX_PRICE:
        day += 1
        if random.randint(1, 2) == 1:
            price_change = random.uniform(0, MAX_INCREASE)
        else:
            price_change = random.uniform(-MAX_DECREASE, 0)

        price *= (1 + price_change)
        print("On day {} price is ${:,.2f}".format(day, price), file=out_file)

    out_file.close()


main()
