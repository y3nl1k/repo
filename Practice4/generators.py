#squares up to N
def sq_gen(n):
    for i in range(n + 1):
        yield i**2

n = int(input("N: "))
for x in sq_gen(n): print(x)

#evens from 0 to n
def evens(n):
    for i in range(0, n + 1, 2):
        yield str(i)

n = int(input("n: "))
print(", ".join(evens(n)))

#div by 3 and 4
def div_3_4(n):
    for i in range(n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i

n = int(input("n: "))
print(*(div_3_4(n)))

#squares with for
def squares(a, b):
    for i in range(a, b + 1):
        yield i**2

a, b = map(int, input("a b: ").split())
for s in squares(a, b):
    print(s)

#down to 0
def countdown(n):
    while n >= 0:
        yield n
        n -= 1

n = int(input("n: "))
print(*(countdown(n)))
