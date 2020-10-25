import random

loops = 10000
sum = 0
cnt = 0

for i in range (loops):
    a = random.randint(1, 20)
    b = random.randint(1, 20)
    c = random.randint(1, 20)

    if a > b: sum += a - c
    else: sum += b - c

    if (c > a and c > b): cnt+=1

print("Average improvement: %f\nPercentage better single: %.2f%%" %(sum / loops, cnt/loops*100))

