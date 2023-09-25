class Car:

    def __init__(self, make, model, year, engine, horsepower, max_speed, mpg, seating):
        self.make = make
        self.model = model
        self.year = year
        self.engine = engine
        self.horsepower = horsepower
        self.max_speed = max_speed
        self.mpg = mpg
        self.seating = seating


    def acceleration_0_60(self):
        return "0-60 (sec): 4.3 (4.5 with T/C on)"


car1 = Car('Mercedes-Benz', 'S63 AMG', 2011, 'V8, Twin Turbo, 5.5L', 536, 180, 18, 5)
car2 = Car('BMW', 'M5', 2008, 'V10 5.0L', 500, 190, 13, 5)

print(car1.make, car1.model)

class EV(Car):
    def __init__(self, make, model, year, horsepower, max_speed, distance, seating):
        super().__init__(make, model, year, horsepower, max_speed, seating)
        self.distance = distance


car3 = Car('Tesla', 'Model S', 2018, 483, 155, 335, 5)
