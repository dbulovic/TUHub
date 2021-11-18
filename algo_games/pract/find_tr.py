from itertools import permutations, combinations
from math import sqrt

leng = 7
cor = [i for i in range(leng**2)]

per = list(combinations(cor, 3))

eql = []

for p in per:
  tril = list(p)
  y1 = tril[0] // leng
  x1 = tril[0] % leng
  y2 = tril[1] // leng
  x2 = tril[1] % leng
  y3 = tril[2] // leng
  x3 = tril[2] % leng

  if x1 > y1 or x2 > y2 or x3 > y3:
    continue

  x1_s = x1 + (leng - 1 - y1)/2
  x2_s = x2 + (leng - 1 - y2)/2
  x3_s = x3 + (leng - 1 - y3)/2

  y1_s = y1 - 0.1339760000001133*y1
  y2_s = y2 - 0.1339760000001133*y2
  y3_s = y3 - 0.1339760000001133*y3

  side1 = sqrt((x1_s - x2_s)**2 + (y1_s-y2_s)**2)
  side2 = sqrt((x2_s - x3_s)**2 + (y2_s-y3_s)**2)
  side3 = sqrt((x3_s - x1_s)**2 + (y3_s-y1_s)**2)

  if abs(side1 - side2) < 0.00001 and abs(side1 - side3) < 0.00001 and abs(side3 - side2) < 0.00001:
    eql.append([[x1, y1],[x2, y2],[x3, y3]])

#print(eql)

albet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'x', 'm']
for y in range(leng):
  offset = leng - y
  for i in range(offset): print(" ", end='')
  for x in range(y + 1):
      print(albet[int(x + (y * (y + 1) / 2))], end=' ')
  print()
