# Parent class 1
class Phone:
    def call(self):
        print("Making a phone call...")

# Parent class 2
class Camera:
    def take_photo(self):
        print("Taking a photo... Cheese!")

# Child class inheriting from both
class Smartphone(Phone, Camera):
    def browse_internet(self):
        print("Browsing the web on a smartphone.")

# Testing multiple inheritance
my_phone = Smartphone()

my_phone.call()         # From Phone
my_phone.take_photo()   # From Camera
my_phone.browse_internet() # From Smartphone