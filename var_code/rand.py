import random

loops = 100000
sum = 0

num = [0 for i in range (20)]


for i in range (loops):
    a = random.randint(1, 20)
    b = random.randint(1, 20)
    if a > b: 
        sum += a
        num[a - 1] += 1
    else:
        sum += b
        num[b - 1] += 1

print ("E. value:", sum / loops)
for i in range (20):
    print("%02d: %.2f"% (i+1, num[i]/loops*100))

