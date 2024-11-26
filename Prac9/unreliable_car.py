from Prac9.car import Car
import random


class UnreliableCar(Car):
    def __init__(self, name, fuel, reliability: float):
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        random_number = random.randint(0, 100)
        if random_number >= self.reliability:
            distance = 0
        drive_distance = super().drive(distance)
        return drive_distance
