class B():
    def __init__(self, bricks):
        self.bricks = bricks
    def isAir(self, x, y):
        return self.bricks[x][y] == '.'
    def isRock(self, x, y):
        return not self.isAir(x, y)
def getInput():
    R, C, F = map(int, input().split())
    bricks = []
    for i in range(R):
        bricks.append(input())
    b = B(bricks)
    return R, C, F, b
R, C, F, b = getInput()
ans = 0
cache = {}
# complex = 0
def dp(i, j, is_left, count):
    '''
    i, j: location
    left: direction of man
    count: the number last time digged
    digged: all bricks digged
    '''
    # global complex
    def calf(x, y):
        k = 0
        while x + k + 1 <= R - 1 and b.isAir(x + k + 1, y):
            k += 1
        return k + 1

    # 0. if row/ i == R, means reach the bottom
    if i == R - 1:
        return 0
    # 00.check cache
    if (i, j, is_left, count) in cache:
        # complex += 1

        return cache[(i, j, is_left, count)]

    # 1. Explore walk space of left and right
    left, right = j, j
    airs = range(j - count + 1, j + 1) if is_left else range(j, j + count)
    # if is_left:
    #     left, right = j - count + 1, j
    # else:
    #     left, right = j, j + count - 1

    while left > 0 and (b.isAir(i, left - 1) or left - 1 in airs) and b.isRock(i + 1, left - 1):
        left -= 1
    while right < C - 1 and (b.isAir(i, right + 1) or left - 1 in airs) and b.isRock(i + 1, right + 1):
        right += 1

    # 2.call next layer dp
    ans = R * C
    for j in range(left, right + 1):
        # left
        for n_count in range(1, j - left + 1):
            f = calf(i + 1, j - 1)
            if f <= F:
                res = dp(i + f, j - 1, is_left=True, count=n_count)
                ans = min(ans, res + n_count)
           
        # right
        for n_count in range(1, right - j + 1):
            f = calf(i + 1, j + 1)
            if f <= F:
                res = dp(i + f, j + 1, is_left=False, count=n_count)
                ans = min(ans, res + n_count)
            

    # left most is a hole
    if left > 0 and b.isAir(i + 1, left - 1) and (b.isAir(i, left - 1) or left - 1 in airs):
        f = calf(i + 1, left - 1)
        if f <= F:
            res = dp(i + f, left - 1, is_left=True, count=0)
            ans =  min(ans, res)

    # right most is a hole
    if right < C - 1 and b.isAir(i + 1, right + 1) and (b.isAir(i, right + 1) or right + 1 in airs):
        f = calf(i + 1, right + 1)
        if f <= F:
            res = dp(i + f, right + 1, is_left=False, count=0)
            ans = min(ans, res)

    # 3. set cache and return
    cache[(i, j, is_left, count)] = ans
    return cache[(i, j, is_left, count)]

# for row in range(R):
#     # face right
#     for rock in range(C - 1):
#         if b.isAir(row + 1, rock): continue 
#         for right in range(rock + 1, C):
#             count = right - rock
#             digged = R * C
#             if row > 1:
#                 if rock > 0:
#                     digged = min(digged, dp[(row - 1, rock - 1)] + 
#     # face left
#     for left in range(0, C - 1):
#         for right in range(left + 1, C)

final = dp(0, 0, is_left=False, count=1)
if final == R * C:
    print('No')
else:
    print('Yes', final)
    # print(complex)

