from Prac9.unreliable_car import UnreliableCar
MANY_TEST = 10
FUEL = 100


def main():
    unreliable_car = UnreliableCar("Prius 1", FUEL, 50.5)
    reliable_car = UnreliableCar("Prius 2", FUEL, 90)
    print(unreliable_car)
    print(reliable_car)


main()
