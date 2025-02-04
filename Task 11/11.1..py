class Car :
    # Define the class constructor
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
    
    def car_brand(self):
        print("The car brand is: ", self.brand)
    
    def car_model(self):
        print("The car model is: ", self.model)

    def car_year(self):
        print("The car year is: ", self.year)

    def display_car_details(self):
        self.car_brand()
        self.car_model()
        self.car_year()


class ElectricCar(Car):
    def __init__(self, brand, model, year, battery_size):
        super().__init__(brand, model, year)
        self.battery_size = battery_size
        self.display_car_details()

    def battery_size(self):
        print("The battery size is: ", self.battery_size)

    def display_car_details(self):
        super().display_car_details()
        print("The battery size is: ", self.battery_size)


car_object = Car("Toyota", "Corolla", 2015)

electric_car_object = ElectricCar("Tesla", "Model S", 2020, 100)