sequence = input()

ca, cb, cc = 0, 0, 0
maxCount = 0
for seq in sequence:
    if seq == 'A':
        ca += 1
    elif seq == 'B':
        cb += 1
    else:
        cc += 1
    if min(ca, cb, cc) == 1:
        ca -= 1
        cb -= 1
        cc -= 1
    maxCount = max(maxCount, max(ca, cb, cc))

print(maxCount)