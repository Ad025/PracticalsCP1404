from Prac_6.guitar import Guitar

CURRENT_YEAR = 2019
VINTAGE = 50


def run_tests():
    """Tests for Guitar class."""
    name = "Gibson L-5 CES"
    year = 1922
    cost = 16035.40

    guitar = Guitar(name, year, cost)
    other = Guitar("Another Guitar", 2012, 1512.9)

    print("{} get_age() - Expected {}. Got {}".format(guitar.name, CURRENT_YEAR - year, guitar.get_age()))
    print("{} get_age() - Expected {}. Got {}".format(other.name, CURRENT_YEAR - year, other.get_age()))
    print()
    print("{} is_vintage() - Expected {}. Got {}".format(guitar.name, True, guitar.is_vintage()))
    print("{} is_vintage() - Expected {}. Got {}".format(other.name, False, other.is_vintage()))

if __name__ == '__main__':
    run_tests()
