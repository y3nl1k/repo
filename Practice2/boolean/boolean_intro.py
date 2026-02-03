#We can evaluate any expression in Python, and get one of two answers, True or False.
print(10 > 9)
print(10 == 9)
print(10 < 9)

#Evaluate a string and a number:
print(bool("Hello"))
print(bool(15))

#The following will return True:
bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])

#The following will return False:
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})