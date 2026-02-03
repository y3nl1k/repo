#Do not print banana:

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)


#Skip the iteration if the variable i is 3, but continue with the next iteration:

for i in range(9):
  if i == 3:
    continue
  print(i)