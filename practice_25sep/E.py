
class Grid():
    def __init__(self, N, M) -> None:
        self.arr2d = []
        self.N = N
        self.M = M
        self.pathFrom = [['.' for x in range(M)] for i in range(N)]
        self.visited = [[False for x in range(M)] for i in range(N)]
        self.door = None
    def addRow(self, rowList):
        self.arr2d.append(rowList)

    def getPeople(self):
        return self.pCount
    
    def findDoor(self):
        for i in range(N):
            for j in range(M):
                if self.arr2d[i][j] != "#":
                    if i == 0:
                        self.pathFrom[i][j] = 'U'
                        self.door = (i, j)
                    elif i == N - 1:
                        self.pathFrom[i][j] = 'D'
                        self.door = (i, j)
                    elif j == 0:
                        self.pathFrom[i][j] = 'L'
                        self.door = (i, j)
                    elif j == M - 1:
                        self.pathFrom[i][j] = 'R'
                        self.door = (i, j)
                    
                if self.door != None:
                    return self.door

    def setVisited(self, cell):
        self.visited[cell[0]][cell[1]] = True
    
    def generatePath(self, location):
        strPath = "";
        while location != self.door:
            x, y = location
            sign = self.pathFrom[x][y]
            strPath += sign
            if sign == "L":
                location = (x, y - 1)
            elif sign == "R":
                location = (x, y + 1)
            elif sign == "U":
                location = (x - 1, y)
            else:
                location = (x + 1, y)
        return strPath + self.pathFrom[self.door[0]][self.door[1]]

    def getCell(self, cell):
        return self.arr2d[cell[0]][cell[1]]

    def findNeighbors(self, location):
        x, y = location
        all_nb = []
        if x + 1 < self.N and self.arr2d[x + 1][y] != '#':
            all_nb.append((x + 1, y))
        if x - 1 >= 0 and self.arr2d[x - 1][y] != '#':
            all_nb.append((x - 1, y))
        if y + 1 < self.M and self.arr2d[x][y + 1] != '#':
            all_nb.append((x, y + 1))
        if y - 1 >= 0 and self.arr2d[x][y - 1] != '#':
            all_nb.append((x, y - 1))

        nbs = []
        for nb in all_nb:
            char = self.arr2d[nb[0]][nb[1]]
            if char != '#' and not self.visited[nb[0]][nb[1]]:
                self.setVisited(nb)
                self.setPathFrom(nb, location)

                nbs.append(nb)

        return nbs


    def setPathFrom(self, to, fr):
        if fr[0] == to[0]:
            if fr[1] + 1 == to[1]:
                sign = "L"
            else:
                sign = 'R'
        elif fr[0] + 1 == to[0]:
            sign = "U"
        else:
            sign = "D"
            
        self.pathFrom[to[0]][to[1]] = sign

class People():
    def __init__(self) -> None:
        self.p = []
        self.dict = {}
        self.maxLenOfP = 0

    def add(self, index, x, y):
        self.p.append((x, y))
        self.dict[(x, y)] = index

    def getIndex(self, x, y):
        return self.dict.get((x, y))
    
    def setPeopleNumber(self, num):
        self.path = [-1] * num

    def setStrPath(self, location, str):
        if len(str) < self.maxLenOfP + 1:
            str = "." * (self.maxLenOfP + 1 - len(str)) + str
        self.path[self.getIndex(location[0], location[1])] = str

        self.maxLenOfP = max(self.maxLenOfP, len(str))
        
    def outputPath(self):
        # not all people have path
        if self.path.count(-1) != 0:
            print(-1)
            return
        
        maxLen = max([len(p) for p in self.path])
        print(maxLen)
        for p in self.path:
            print(p + (maxLen - len(p)) * '.')


N, M = [int(x) for x in input().split()]


grid = Grid(N, M)
people = People()
# get input
index = 0
for i in range(N):
    rowStr = input()
    # find people and add to people
    for j in range(M):
        if rowStr[j] == 'P':
            people.add(index, i, j)
            index += 1
    # add to grid
    grid.addRow(rowStr)

# Set the number of people
people.setPeopleNumber(index)

# do BFS
door = grid.findDoor()

stack = [door]
grid.setVisited(door)
if grid.getCell(door) == 'P':
    pathStr = grid.generatePath(door)
    people.setStrPath(door, pathStr)

while stack != []:

    newStack = []
    for cell in stack:
        for neighbor in grid.findNeighbors(cell):
            if grid.getCell(neighbor) == 'P':
                pathStr = grid.generatePath(neighbor)
                people.setStrPath(neighbor, pathStr)
                

            newStack.append(neighbor)
            grid.setVisited(neighbor)
    stack = newStack
people.outputPath()