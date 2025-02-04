class Car :
    # Define the class constructor
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

        self.car_brand()
        self.car_model()
        self.car_year()
    
    def car_brand(self):
        print("The car brand is: ", self.brand)
    
    def car_model(self):
        print("The car model is: ", self.model)

    def car_year(self):
        print("The car year is: ", self.year)



car_object = Car("Toyota", "Corolla", 2015)