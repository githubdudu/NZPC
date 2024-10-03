R, C, D, N = [int(x) for x in input().split(' ')]


# prepare matrix
index = []
dist = D * D
min_j = 0
for i in range(D + 1):
    ysqr = (D - i) ** 2

    for j in range(min_j, D + 1):
        xsqr = j ** 2
        if ysqr + xsqr <= dist:
            min_j = j
        else:
            break;
           
    index.append(min_j)

# print(index)
students = []
for i in range(N):
    x, y = [int(x) for x in input().split(" ")]
    students.append((x- 1, y -1))

covers = {}
for x, y in students:
    for i in range(max(0, x - D), min(x + D + 1, R)):
        dy = index[D - abs(x - i)]
        inc_y = max(0, y - dy)
        dec_y = min(C, y + dy + 1)
        for j in range(inc_y, dec_y):
            if (i, j) in covers:
                covers[(i, j)] += 1
            else:
                covers[(i, j)] = 1
def problem():
    minRes = N
    for i in range(R):
        for j in range(C):
            if (i, j) in students: continue
            if (i, j) not in covers == 0:
                print(0)
                return
            minRes = min(minRes, covers[(i, j)])
    print(minRes)
problem()
# for i in range(R):
#     for j in range(C):
#         if (i, j) in students:
#             continue
#         count = 0
#         for x, y in students:
#             dx, dy = abs(x - i), abs(y - j)
#             if dx <= D and dy <= index[D - dx]:
#                 count += 1
#         minRes = min(count, minRes)

