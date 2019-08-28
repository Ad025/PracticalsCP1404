
price = float(input("Enter price per kWh in cents:"))
use = float(input("Enter daily use per kWh:"))
days = int(input("Number of days in the billing period:"))

price_in_dollars = price / 100
total = price_in_dollars * use * days
print("Estimated bill: ${}".format(total))