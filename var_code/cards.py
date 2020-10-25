import random

cards = [False for i in range (4)]
for i in  range (len(cards)):
    ca = random.random()
    if ca > 0.5: 
        cards[i] = True
