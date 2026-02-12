#Sort a list of tuples by the second element:
students = [("Emil", 25), ("Tobias", 22), ("Linus", 28)]
sorted_students = sorted(students, key=lambda x: x[1])
print(sorted_students)


#Sort strings by length:
words = ["apple", "pie", "banana", "cherry"]
sorted_words = sorted(words, key=lambda x: len(x))
print(sorted_words)


#Sort a list of dictionaries by a specific key
students = [
    {"name": "Yenlik", "grade": 95},
    {"name": "Alice", "grade": 88},
    {"name": "Bob", "grade": 99}
]
by_grade = sorted(students, key=lambda s: s["grade"], reverse=True)
print(by_grade)