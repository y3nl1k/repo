#Functions can return values using the return statement:
def my_function(x, y):
  '''
  returns the sum of 2 arguments
  '''
  return x + y

result = my_function(5, 3)
print(result)


#A function that returns a list:
def my_function():
  return ["apple", "banana", "cherry"]

fruits = my_function()
print(fruits[0])
print(fruits[1])
print(fruits[2])


#returning a tuple
def my_function():
  return (10, 20)

x, y = my_function()
print("x:", x)
print("y:", y)
 

#the default return is None
def say_hello(name):
    print(f"Hello, {name}!")

result = say_hello("cool ahh name")
print(result)

