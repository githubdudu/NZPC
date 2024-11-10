N = int(input())

sheet = []
for i in range(N):
    cell = int(input())
    if sheet == [] or sheet[-1] != cell:
        sheet.append(cell)
if sheet[0] != 0:
    sheet.insert(0, 0)
if sheet[-1] != 0:
    sheet.append(0)

diction = [[-1] * len(sheet) for _ in range(len(sheet))]
def minEdit(l, r):
    if l > r: return 0;
    elif l == r: return 1;

    if diction[l][r] != -1:
        return diction[l][r]

    c = sheet[l]
    
    minCount = 1 + minEdit(l + 1, r);
    # get all indexes of c
    for i in range(l + 1, r + 1):
        if c == sheet[i]:
            # cut one: divide it into two sub-problem
            minCount = min(minCount, 1 + minEdit(l + 1, i - 1) + minEdit(i + 1, r))
            # cut two: c has been printed for second problem
            minCount = min(minCount, minEdit(l + 1, i - 1) + minEdit(i, r))
    # update dict
    diction[l][r] = minCount
    return minCount

print(minEdit(0, len(sheet) - 1) - 1)