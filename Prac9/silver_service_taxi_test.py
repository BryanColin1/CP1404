from Prac9.silver_service_taxi import SilverServiceTaxi


def main():
    silver_service_taxi = SilverServiceTaxi("Silver Car", 200, 4)
    print(silver_service_taxi)
    silver_service_taxi.drive(18)
    print(f"Fare = {silver_service_taxi.get_fare()}")


main()
