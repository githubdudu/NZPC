# Box and Arrow Diagram

# GET input
N, M = [int(x) for x in input().split()]


class Boxes():
    def __init__(self, N) -> None:
        self.fromPaths = [[] for x in range(N)]
        self.aliveArrowCount = [0] * N

    def addPath(self, _from, _to):
        self.fromPaths[_from].append(_to)
    def getPath(self, _from):
        return self.fromPaths[_from]
    
    def alive(self, node):
        return node == 1 or self.aliveArrowCount[node] > 0
    def getAliveCount(self, node):
        return self.aliveArrowCount[node]
    def increaseAliveCount(self, node):
        self.aliveArrowCount[node] += 1

class Arrows():
    def __init__(self, M) -> None:
        self.arrows = [-1]
        self.arrowAdded = [True] * M
        
    def addArrow(self, _from, _to):
        self.arrows.append((_from, _to))

    def setArrowUsed(self, X, val):
        self.arrowAdded[X] = val

    def getArrow(self, i):
        return self.arrows[i]
    
    def arrowUsed(self, i):
        return self.arrowAdded[i]
# fromPaths = [[] for x in range(N + 1)]
# aliveArrowCount = [0] * (N + 1)

# arrows = [-1]
# arrowsUsed = [True] * (M + 1)

boxes = Boxes(N + 1)
arrows = Arrows(M + 1)

for i in range(M):
    _from, _to = [int(x) for x in input().split()]
    arrows.addArrow(_from, _to)

Q = int(input())
queries = []
for i in range(Q):
    C, X = [int(x) for x in input().split()]
    queries.append((C, X))
    if C == 1:
        arrows.setArrowUsed(X, False)

# Build path: from bottom to top
# which means change the deletion to addition

# build the path of graph that after all deletion
for i in range(1, M + 1):
    _from, _to = arrows.getArrow(i)
    if arrows.arrowUsed(i):
        boxes.addPath(_from, _to)

# inital the graph that after all deletion
stack = [1]
while stack != []:
    node = stack.pop(-1)
    for next in boxes.getPath(node):
        if boxes.alive(next):
            boxes.increaseAliveCount(next)
        else:
            boxes.increaseAliveCount(next)
            stack.append(next)

answers = []
for C, X in reversed(queries):
    if C == 1:
    # addition of the deleted one
        _from, _to = arrows.getArrow(X)

        boxes.addPath(_from, _to)
        if boxes.alive(_from) and boxes.alive(_to):
            boxes.increaseAliveCount(_to)
        elif boxes.alive(_from) and not boxes.alive(_to):
            boxes.increaseAliveCount(_to)
            stack = [_to]
            while stack != []:
                node = stack.pop(-1)
                for next in boxes.getPath(node):
                    if boxes.alive(next):
                        boxes.increaseAliveCount(next)
                    else:
                        boxes.increaseAliveCount(next)
                        stack.append(next)
    else:
    # query
        answers.append(boxes.getAliveCount(X))



for answer in reversed(answers):
    print(answer)