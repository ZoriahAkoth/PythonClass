class Car:
    model = "V8 2018 XX"
    brand = "Toyota"
    number_plate = "KDQ 809R"
    color = "white"
    mileage = 110
    cc = 4000

    def car_profile(self):
        print(self.brand)
        print(self.model)
        print(self.number_plate)
        print(self.cc)

    def check_mileage(self):
        print(self.mileage)

    def update_mileage(self,new_mileage):
        self.mileage = new_mileage

#class instance
car = Car()
print("CAR")
car.car_profile()

harrier = Car()
print("HARRIER")
harrier.model = "Harrier 2010"
harrier.color = "pink"
harrier.mileage = 300
harrier.car_profile()
car.car_profile()

forester = Car()
forester.brand = "Honda"
forester.color = "yellow"
forester.cc = 2500