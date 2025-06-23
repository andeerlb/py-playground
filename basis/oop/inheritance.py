# %%
class Car:
    def __init__(self, brand: str, model: str, year: int):
        self.brand = brand
        self.model = model
        self.year = year

    def print_car(self):
        print(f"brand: {self.brand}\nmodel:{self.model}\nyear:{self.year}\n")

car = Car("byd","song plus", 2025)
car.print_car()

class Caoa(Car):
    pass

car = Caoa("caoa", "tiggo 7 sport", 2025)
car.print_car()

class Hyundai(Car):
    def __init__(self, model: str, year: int):
        Car.__init__(self, "hyundai", model, year)

car = Hyundai("hb20", 2019)
car.print_car()

class ToyotaYaris(Car):
    def __init__(self, year: int):
        super().__init__("toyota", "yaris", year)

car = ToyotaYaris(2022)
car.print_car()
# %%
