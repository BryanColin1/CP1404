from Prac9.taxi import Taxi

FLAGFALL = 4.50


class SilverServiceTaxi(Taxi):

    def __init__(self, name, fuel, fanciness: float):
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km *= fanciness

    def __str__(self):
        return f"{super().__str__()} plus flagfall of ${FLAGFALL}"

    def get_fare(self):
        return super().get_fare() + FLAGFALL
