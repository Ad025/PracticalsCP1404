from Prac_8.taxi import Taxi


def main():
    my_taxi = Taxi("prius 1", 100)
    my_taxi.drive(40)
    print(my_taxi)
    my_taxi.start_fare()
    my_taxi.drive(100)
    print(my_taxi)


main()
