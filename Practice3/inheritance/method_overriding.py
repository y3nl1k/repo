class Animal:
    def speak(self):
        print("The animal makes a sound")

class Dog(Animal):
    # Overriding the speak method
    def speak(self):
        print("The dog barks: Woof! Woof!")

class Cat(Animal):
    # Overriding the speak method
    def speak(self):
        print("The cat meows: Meow!")

# Testing overriding
generic_animal = Animal()
my_dog = Dog()
my_cat = Cat()

generic_animal.speak() # Parent version
my_dog.speak()         # Overridden version
my_cat.speak()         # Overridden version