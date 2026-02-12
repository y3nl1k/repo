#Double all numbers in a list:
numbers = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, numbers))
print(doubled)


#Apply 12% tax to prices
prices = [1000, 2500, 5000]
final_prices = list(map(lambda p: p * 1.12, prices))
print(final_prices)