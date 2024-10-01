class IO:
    def getStr(self):
        return input().strip()
    def getInt(self):
        return int(input().strip())
    def getStrList(self):
        return self.getStr().split(" ")
    def getIntList(self):
        return [int(x) for x in self.getStrList()]
    def strTuple(self, tuple):
        return "%s %s" % tuple
    def strList(self, li):
        return " ".join(map(str, li))
io = IO()

T = io.getInt()

def problem_E():
    for _ in range(T):
        N = io.getInt()
        nodes = [[] for x in range(N + 1)]
        for _ in range(N - 1):
            _from, _to = io.getIntList()
            nodes[_from].append(_to)
            nodes[_to].append(_from)
        
        # find leaves
        leaves = [False] * (N + 1)
        for i in range(2, N + 1):
            if len(nodes[i]) == 1:
                leaves[i] = True
        
        # bfs
        stack = [1]
        visited = [False] * (N + 1)
        visited[1] = True
        roots = [0] * (N + 1)
        all_stack = []

        # use BFS again
        while stack != []:
            new_stack = []
            for node in stack:
                for next in nodes[node]:
                    if not visited[next]:
                        new_stack.append(next)
                        roots[next] = node
                        visited[next] = True
            all_stack.append(stack[:])
            stack = new_stack

        mx_counts = 0
        node_set = set()
        while all_stack != []:
            stack = all_stack.pop()
            # add the nodes from this depth to root
            for node in stack:
                while node != 0 and node not in node_set:
                    node_set.add(node)
                    node = roots[node]

            mx_counts = max(mx_counts, len(node_set))
            # remove node that at this depth
            for node in stack:
                node_set.remove(node)
            
        print(N - mx_counts)

problem_E()