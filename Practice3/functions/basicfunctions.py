#This creates a function named my_function that prints "Hello from a function" when called.
def my_function():
    print("Hello from a function")
my_function()


#we can call a function mulpitple times 
my_function()
my_function()


#With functions - reusable code:
def fahrenheit_to_celsius(fahrenheit):
  return (fahrenheit - 32) * 5 / 9

print(fahrenheit_to_celsius(77))


#Function definitions cannot be empty. If you need to create a function placeholder without any code, use the pass statement:
def my_function():
  pass