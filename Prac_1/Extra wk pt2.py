def main():
    TARIFF_11 = 0.244618
    TARIFF_12 = 0.136928

    tariff = int(input("which tariff? 11 or 12:"))
    while tariff != 11 and tariff != 12:
        print("invalid")
        tariff = int(input("which tariff? 11 or 12:"))

    use = float(input("Enter daily use per kWh:"))
    days = int(input("Number of days in the billing period:"))

    if tariff == 11:
        cost = TARIFF_11
        total = cost * use * days
    elif tariff == 12:
        cost = TARIFF_12
        total = cost * use * days

    print("Estimated bill: ${:.2f}".format(total))


main()
