class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage

    def the_cars(self):
        print(f"The {self.color} car has {self.mileage} miles.")


brand1 = Car("blue", '20,000')
brand1.the_cars()

brand2 = Car("red", '30,000')
brand2.the_cars()








