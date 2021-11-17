from itertools import permutations, combinations
from math import sqrt

leng = 2
i = 0
for y in range(leng):
    for x in range(y + 1):
        print("x", end=' ')
        i = i+1
    print()

cor = [i for i in range(leng**2)]

per = list(permutations(cor, 3))

eql = []

for p in per:
  tril = list(p)
  x1 = tril[0] // leng
  y1 = tril[0] % leng
  x2 = tril[1] // leng
  y2 = tril[1] % leng
  x3 = tril[2] // leng
  y3 = tril[2] % leng

  if x1 > y1 or x2 > y2 or x3 > y3:
    continue

  side1 = sqrt((x1 - x2)**2 + (y1-y2)**2)
  side2 = sqrt((x2 - x3)**2 + (y2-y3)**2)
  side3 = sqrt((x3 - x1)**2 + (y3-y1)**2)

  tri= [side1, side2, side3]
  tri.sort()

  if tri[0] < tri[1]+tri[2]:
    if tri[0] == tri[2]:
      continue
    elif tri[1] == tri[2] or tri[1] == tri[0]:
      if abs(tri[2]**2 - tri[1]**2 - tri[0]**2) < 0.0001:
        eql.append([[x1, y1],[x2, y2],[x3, y3]]) 

print(eql)
