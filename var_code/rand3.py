from random import randint

loops = 6
sum = 0
res = [0 for i in range (6)]

for i in range (loops):
    sum = 0
    a = randint(1, 6)
    b = randint(1, 6)
    c = randint(1, 6)
    d = randint(1, 6)
    sum += a + b + c + d - min(a, b, c, d)
    res[i] = sum
for i in res:
    print(i)
