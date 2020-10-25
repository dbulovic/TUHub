import random

loops = 1000000
valid = 0
for i in range(loops):
    a = random.random()
    b = random.random()
    x1 = min(a, b)
    x2 = 1.0 - max(a, b)
    x3 = 1.0 - x1 - x2
    if(x1 + x2 > x3 and x1 + x3 > x2 and x2 + x3 > x1):
        valid += 1
print(valid / loops)