#Comparison operators return True or False based on the comparison:

x = 5
y = 3

print(x == y)
print(x != y)
print(x > y)
print(x < y)
print(x >= y)
print(x <= y)


#Python allows you to chain comparison operators:

x = 5

print(1 < x < 10)
print(1 < x and x < 10)


#Test if a number is greater than 0 and less than 10:

x = 5
print(x > 0 and x < 10)


#Test if a number is less than 5 or greater than 10:

x = 5
print(x < 5 or x > 10)


#Reverse the result with not:

x = 5
print(not(x > 3 and x < 10))