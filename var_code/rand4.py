import random

sum = 0

for i in range (10000):
    a = random.randint(1, 20)
    b = random.randint(1, 20)
    if a > b:
        sum += a - b 
    else:
        sum += b - a

print(sum/10000)