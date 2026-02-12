#Filter out even numbers from a list:
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))
print(odd_numbers)

#Filter words longer than 5 letters
words = ["apple", "banana", "kiwi", "cherry", "pear"]
long_words = list(filter(lambda w: len(w) > 5, words))
print(long_words)


