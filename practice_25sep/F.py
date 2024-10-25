N = int(input())

class Graph():
    def __init__(self, N) -> None:
        self.paths = [[] for x in range(N + 1)]
        self.visited = [False for x in range(N + 1)]
        self.leaves = {}
        self.parent = [-1 for x in range(N + 1)]
        self.answer = []

    def addPath(self, path) -> None:
        _fr, _to = [int(x) for x in path.split()]

        self.paths[_fr].append(_to);
        self.paths[_to].append(_fr);
    
    def degree(self, node) -> int:
        return len(self.neighbours(node))
    
    def neighbours(self, node) -> list[int]:
        return self.paths[node]
    
    def isLeaf(self, node):
        return self.degree(node) == 1
    
    def addCity(self, city, node):
        if node in graph.leaves:
            prev = graph.leaves.get(node)
            if len(city) == 2:
                if len(prev) == 2:
                    self.answer.append((prev[1], city[0]))
                    prev[1] = city[1]

                elif len(prev) == 1:
                    self.answer.append((prev[0], city[0]))
                    prev[0] = city[1]
            elif len(city) == 1:
                if len(prev) == 1:
                    prev.append(city[0])
                elif len(prev) == 2:
                    self.answer.append((prev[1], city[0]))
                    prev.pop(-1)
            
        else:
            graph.leaves[node] = city
    
    
graph = Graph(N)

for i in range(N - 1):
    graph.addPath(input())

# ths leavesf
stack = [1] # using stack to simulate the 


while True:
    node = stack[-1]
    if graph.visited[node]:
        # pop stack and get the unpaired cities
        stack.pop(-1)
        leaves = graph.leaves.pop(node)

        # escalate to parent node of city
        parent = graph.parent[node]
        
        graph.addCity(leaves, parent)
            
    else: # not visited
        graph.visited[node] = True

        for n in graph.neighbours(node):
            if not graph.visited[n]:
                # leaves
                if graph.isLeaf(n):
                    graph.addCity([n], node)

                # non-leaves add to stack
                else:
                    stack.append(n)
                    graph.parent[n] = node

    if len(stack) == 1: break;
# deal with last node:

if len(graph.leaves[1]) == 1:
    graph.answer.append((1, graph.leaves[1][0]))
else:
    if graph.isLeaf(1):
        graph.answer.append((1, graph.leaves[1][0]))
        graph.answer.append((1, graph.leaves[1][1]))
    else:
        graph.answer.append((graph.leaves[1][0], graph.leaves[1][1]))

print(len(graph.answer))
[print(*i) for i in graph.answer]
