# Example 1: Person class with various methods
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Simple method
    def greet(self):
        print(f"Hello, my name is {self.name}")

    # Method accessing and returning properties
    def get_info(self):
        return f"{self.name} is {self.age} years old"

    # Method that modifies an attribute
    def celebrate_birthday(self):
        self.age += 1
        print(f"Happy birthday! {self.name} is now {self.age}")

    # Special string representation method
    def __str__(self):
        return f"{self.name} ({self.age})"

# Using Person class
p1 = Person("Tobias", 36)
p1.greet()
print(p1.get_info())
p1.celebrate_birthday()
print(p1)

# Example 2: Calculator class with parameters in methods
class Calculator:
    def add(self, a, b):
        return a + b

    def multiply(self, a, b):
        return a * b

calc = Calculator()
print("Addition:", calc.add(10, 5))
print("Multiplication:", calc.multiply(4, 7))

#Create multiple methods in a class:

class Playlist:
  def __init__(self, name):
    self.name = name
    self.songs = []

  def add_song(self, song):
    self.songs.append(song)
    print(f"Added: {song}")

  def remove_song(self, song):
    if song in self.songs:
      self.songs.remove(song)
      print(f"Removed: {song}")

  def show_songs(self):
    print(f"Playlist '{self.name}':")
    for song in self.songs:
      print(f"- {song}")

my_playlist = Playlist("Favorites")
my_playlist.add_song("Bohemian Rhapsody")
my_playlist.add_song("Stairway to Heaven")
my_playlist.show_songs()