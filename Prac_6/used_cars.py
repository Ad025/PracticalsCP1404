"""CP1404/CP5632 Practical - Client code to use the Car class."""
# Note that the import has a folder (module) in it.

from Prac_6.car import Car


def main():
    """Demo test code to show how to use car class."""
    my_car = Car("Car", 180)
    my_car.drive(30)
    print("fuel =", my_car.fuel)
    print("odo =", my_car.odometer)
    print(my_car)

    print("\n")

    print("Limo")
    limo = Car("Limo", 100)
    limo.add_fuel(20)
    print("fuel =", limo.fuel)
    limo.drive(115)
    print("odo =", limo.odometer)
    print(limo)


main()
