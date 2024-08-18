import math

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

"""
1. (a 2-dimensional array of
altitudes), 
2. 4 neighbouring cells.
3. none of its 4 neighbouring cells has a lower altitude  called a sink.
4. In case of a tie, 
this list: North, West, East, South.

(in particular, the basin of the most North-Western
cell is always labelled 'a'). 
5. Note that neighbouring sinks are not considered to be in
the same drainage basin.

Input
The first line of the input contains two integers – H and W – the height and width of
the map, in cells (1 ≤ H, W ≤ 100). 

"""
H, W = io.getIntList() # in cells (1 ≤ H, W ≤ 100). 
cells = [[] for i in range(H)]
parent = [[] for i in range(H)]
# output
output = [[] for i in range(H)]
for h in range(H):
    cells[h] = io.getIntList()
    output[h] = [0 for w in range(W)]
    parent[h] = [(-1, -1) for w in range(W)]


markers = "abcdefghijklmnopqrstuvwxyz"
markersIdx = 0

"""The next H lines will each contain a row of the
map, from north to south, each containing W integers, from west to east, specifying
the altitudes of the cells (0 ≤ altitudes < 10,000). It is guaranteed that there will be at
most 26 basins.

Output
Output H lines that list the basin labels for each of the cells, in the same order as
they appear in the input."""

def minCell(x, y, newX, newY):
    if cells[newX][newY] <= cells[x][y]:
        return newX, newY
    else:
        return x, y
    
def calParent(x, y):
    tempX, tempY = x, y
    # South
    if x < H - 1:
        tempX, tempY = minCell(tempX, tempY, x + 1, y)
    # East
    if y < W - 1:
        tempX, tempY = minCell(tempX, tempY, x, y + 1)
    # West
    if y > 0:
        tempX, tempY = minCell(tempX, tempY, x, y - 1)
    # North
    if x > 0:
        tempX, tempY = minCell(tempX, tempY, x - 1, y)

    if cells[x][y] == cells[tempX][tempY]:
        return -1, -1
    else:
        return tempX, tempY

def initParent():
    for h in range(H):
        for w in range(W):
            parent[h][w] = calParent(h, w)


def problem():
  
    initParent()

    def marked(x, y) -> bool:
        return output[x][y] != 0

    def findSink(x, y) -> tuple:
        sx, sy = x, y
        while True:
            # In case of a tie, North, West, East, South.
            if parent[sx][sy] == (-1, -1):
                return (sx, sy)
            else:
                sx, sy = parent[sx][sy]

    def mark(tuple) -> None:
        x, y = tuple
        global markersIdx
        marker = markers[markersIdx]
        markersIdx += 1
        

        def helper(x, y, m):

            # mark itself
            if marked(x, y):
                return
            output[x][y] = m
            # iterate its neighbor
            # East
            if y < W - 1 and parent[x][y + 1] == (x, y):
                helper(x, y + 1, m)
            # South
            if x < H - 1 and parent[x + 1][y] == (x, y):
                helper(x + 1, y, m)
            # North
            if x > 0 and parent[x - 1][y] == (x, y):
                helper(x - 1, y, m)
            # West
            if y > 0 and parent[x][y - 1] == (x, y):
                helper(x, y - 1, m)

        helper(x, y, marker)
    # iterate from west to east, N to S

    for h in range(H):
        for w in range(W):
            if not marked(h, w):
                sink = findSink(h, w)
                mark(sink)
                

    for h in range(H):
        print(io.strList(output[h]))
problem()
# 1h, 55min
