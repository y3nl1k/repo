#Create a class named Person, use the __init__() method to assign values for name and age:

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("Emil", 36)

print(p1.name)
print(p1.age)


#A Rectangle class for geometry
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.area = width * height

rect = Rectangle(10, 5)
print(f"Rectangle area: {rect.area}")


#A Music Track class
class Song:
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist

track = Song("Blinding Lights", "The Weeknd")
print(f"Now playing: {track.title} by {track.artist}")