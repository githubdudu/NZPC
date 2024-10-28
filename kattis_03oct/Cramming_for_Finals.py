R, C, D, N = [int(x) for x in input().split(' ')]



min_j = 0

def coverage(D):
    '''
    Returns a array of length [D + 1], which the i-th entry represents
    when the distance between row/line and circle centre is i, the half width of the range that the line inside the circle, aka, the vertical distance between the circle centre and the intersection of circle and line
    '''
    coversMap = []
    D2 = D * D
    max_half_width = D

    for x in range(D + 1):
        xto2 = x * x

        while True:
            yto2 = max_half_width ** 2
            if xto2 + yto2 <= D2:
                coversMap.append(max_half_width)
                break;
            else:
                max_half_width -= 1
    return coversMap;

coversMap = coverage(D)
# print(coversMap, 'covermap')

students = set()
students_row = {}
for i in range(N):
    x, y = [int(x) for x in input().split(" ")]
    x, y = x - 1, y - 1
    students.add((x, y))
    if x in students_row:
        students_row[x].append(y)
    else:
        students_row[x] = [y]

def minInRow(row):
    changes = {}
    def update(diction, K,  V):
        if K in diction:
            diction[K] = diction.get(K) + V
        else:
            diction[K] = V

    for x, y in students:
        dis_x = abs(x - row)
        if dis_x <= D:
            diff_y = coversMap[dis_x]
            low_bound = max(0, y - diff_y)
            update(changes, low_bound, 1)

            if y + diff_y < C - 1:
                update(changes, y + diff_y + 1, -1)

    # print(changes)
    # deal with edge cases
    update(changes, 0, 0)
    if row in students_row:
        for K in students_row.get(row):
            update(changes, K, N)
            if K < C - 1:
                update(changes, K + 1, -N)

    num_can_hear = 0
    min_num = N
    for key in sorted(list(changes)):

        num_can_hear += changes[key]

        if num_can_hear == 0:
            return 0 # short-circuit
        min_num = min(num_can_hear, min_num)
        # print(num_can_hear, end=' ')
    
    return min_num

def problem():
    minRes = N
    for i in range(R):
        minRes = min(minRes, minInRow(i))
        if minRes == 0:
            break;
    print(minRes)
problem()

