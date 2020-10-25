sum = 1
for i in range(23):
    sum *= (365.25 - i)/(365.25)
print(sum) 