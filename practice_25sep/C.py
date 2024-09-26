N = int(input())

NUM = 100
nearest = NUM - 1
minDiff = abs(NUM - 1 - N)

while True:
    newDiff = abs(NUM - 1 - N)
    if newDiff <= minDiff:
        minDiff = newDiff
        nearest = NUM - 1
    else:
        print(nearest)
        break
    
    NUM += 100