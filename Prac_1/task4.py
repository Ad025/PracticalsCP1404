def main():
    sales = float(input("Enter sales:$"))
    while sales >= 0:
        if sales < 1000:
            sale_bonus = (sales * 0.10)
            print("sale bonus is {}".format(sale_bonus))

        else:
            sale_bonus = (sales * 0.15)
            print("Sale bonus is {}".format(sale_bonus))

        sales = float(input("Enter sales:$"))

    print("Bye")


main()
