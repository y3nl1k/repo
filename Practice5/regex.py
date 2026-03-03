import re

n = input()
match = re.search(r'ab*', n)
if match: print(match.group())
else: print("No match")

match = re.search(r'ab{2,3}', n)
if match: print(match.group())
else: print("No match")

match = re.findall(r'\b[a-z]+(?:_[a-z]+)*\b', n)
if match:
    for m in match: print(m)  
else: print("No match")
   

match = re.findall(r'[A-Z][a-z]+', n)
if match:
    for m in match: print(m)
else: print("No match")
    

match = re.search(r'a.*b$', n)
if match: print(match.group())
else: print("No match")

s = re.sub(r',|\.|\s', r':', n)
print(s)

camel = re.sub(r'_([a-z])', lambda m: m.group(1).upper(), n)
print(camel)

s = re.split(r"[A-Z]", n)
for i in s: print(i, end=" ")
print('\n')

spa = re.sub(r'(?<!^)(?=[A-Z])', ' ', n)
print(spa)

snake = re.sub(r'(?<!^)(?=[A-Z])', '_', n).lower()
print(snake)