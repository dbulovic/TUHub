def r(a):
    if a <= 2:
        return 1
    else:
        h = 0
        for i in range(1, 5):
            h += i * r(a - 2)
    return h

print(r(13))       

