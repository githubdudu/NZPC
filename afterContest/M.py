class IO():
    def getStr(self):
        return input().strip()
    
    def getInt(self):
        return int(input().strip())
    
    def getStrList(self):
        return self.getStr().split(' ')
    
    def getIntList(self):
        return [int(x) for x in self.getStrList()]
    
    def strTuple(self, tuple):
        return "%s %s" % tuple
    
    def strList(self, li):
        return " ".join(map(str, li))
io = IO() 

import queue

# Get input
N, M, K = io.getIntList()
grid = []
for _ in range(N):
    line = io.getStr()
    grid.append(line)

# Helper function of grid
def checkGrid(pos):
    x, y = pos
    return grid[x][y]


def problem():
    # dp
    dp0 = [0] * M
    for n in range(N):
        for m in range(M):
            cost = 0 if grid[n][m] == '0' else 1;
            if n == 0 and m == 0:
                dp0[m] = cost
            elif m == 0:
                dp0[m] += cost
            elif n == 0:
                dp0[m] = dp0[m - 1] + cost
            else:
                dp0[m] = min(dp0[m], dp0[m - 1]) + cost
    minK = dp0[M - 1]

    dp1 = [0] * M
    for n in range(N):
        for m in range(M):
            cost = 0 if grid[n][m] == '1' else 1;
            if n == 0 and m == 0:
                dp1[m] = cost
            elif m == 0:
                dp1[m] += cost
            elif n == 0:
                dp1[m] = dp1[m - 1] + cost
            else:
                dp1[m] = min(dp1[m], dp1[m - 1]) + cost
    maxK = N + M - 1 - dp1[M - 1]

    if K >= minK and K <= maxK:
        print(1)
    else:
        print(0)

    # print({minK}, {maxK})
problem()

