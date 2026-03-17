names = ["Alpha", "Bingo", "Charlie"]
scores = [85, 90, 95]
for name, score in zip(names, scores):
    print(f"{name} scored {score}")

for i, name in enumerate(names, 1):
    print(f"Student #{i}: {name}")