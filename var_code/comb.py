import operator as op
from functools import reduce

def ncr(n, r):
    r = min(r, n-r)
    numer = reduce(op.mul, range(n, n-r, -1), 1)
    denom = reduce(op.mul, range(1, r+1), 1)
    return numer // denom

sum = 0

for i in range(1, 4):
    st = ncr(4, i) * (0.9)**(4 - i) * (0.1)**(i)
    print(st)
    sum += ncr(4, i) * (0.9)**(4 - i) * (0.1)**(i)

print(sum, 1- sum)
