class Car:
    # Class Variable: Shared by all cars
    wheels = 4 

    def __init__(self, brand, model):
        # Instance Variables: Unique to each car
        self.brand = brand
        self.model = model

# Create different objects
car1 = Car("Toyota", "Camry")
car2 = Car("Tesla", "Model 3")

# Accessing instance variables
print(f"Car 1: {car1.brand}, Wheels: {car1.wheels}")
print(f"Car 2: {car2.brand}, Wheels: {car2.wheels}")

# Changing a class variable affects all instances
Car.wheels = 6
print(f"After change - Car 1 wheels: {car1.wheels}")
print(f"After change - Car 2 wheels: {car2.wheels}")

# Changing an instance variable only affects that object
car1.brand = "Lexus"
print(f"Car 1 new brand: {car1.brand}")
print(f"Car 2 brand is still: {car2.brand}")