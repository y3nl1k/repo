#Assigning a string to a variable
a = "Hello"
print(a)


#You can use three double quotes:
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)


#Get the characters from position 2 to position 5 (not included):
b = "Hello, World!"
print(b[2:5])


#Get the characters from the start to position 5 (not included):
b = "Hello, World!"
print(b[:5])


#Get the characters from position 2, and all the way to the end:
b = "Hello, World!"
print(b[2:])


#From: "o" in "World!" (position -5)
#To, but not included: "d" in "World!" (position -2):

b = "Hello, World!"
print(b[-5:-2])


#returns the string in upper case:
a = "Hello, World!"
print(a.upper())


#returns the string in lower case:

a = "Hello, World!"
print(a.lpwer())


#removes any whitespace from the beginning or the end:
a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"


#Merge variable a with variable b into variable c:
a = "Hello"
b = "World"
c = a + b
print(c)


#Display the price with 2 decimals:
price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)


#The escape character allows you to use double quotes when you normally would not be allowed:
txt = "We are the so-called \"Vikings\" from the north."