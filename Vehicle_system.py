class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
    
    def get_vehicle_info(self):
        return f"brand:{self.brand}\nmodel:{self.model}\nyear:{self.year}"

class car(Vehicle):
    def __init__(self, num_of_doors, brand, model, year):
        self.num_of_doors = num_of_doors

        Vehicle.__init__(self, brand, model, year)
    
    def get_vehicle_info(self):
        # Override to include the number of doors
        base_info = super().get_vehicle_info()
        print (f"{base_info} \nDoors: {self.num_of_doors}")

class Truck(Vehicle):
    def __init__(self, cargo_capacity, brand, model, year):
        self.cargo_capacity = cargo_capacity
        Vehicle.__init__(self, brand, model, year)

    def get_vehicle_info(self):
        base_info = super().get_vehicle_info()
        print(f"{base_info} \ncapacity: {self.cargo_capacity}kg")

class Motorcycle(Vehicle):
    def __init__(self, type_of_motor, brand, model, year):
        self.type_of_motor = type_of_motor
        Vehicle.__init__(self, brand, model, year)

    def get_vehicle_info(self):
        base_info = super().get_vehicle_info()
        print(f"{base_info} \nengine: {self.type_of_motor}")

car1 = Motorcycle("v8","toyota", "etios", "2014")
car1.get_vehicle_info()