#Print each fruit in a fruit list:

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)


#Loop through the letters in the word "banana":

for x in "banana":
  print(x)


#Increment the sequence with 3 (default is 1):

for x in range(2, 30, 3):
  print(x)


#Print each adjective for every fruit:

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)

