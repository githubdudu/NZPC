N = int(input())

V = [[] for x in range(N)]

for i in range(N - 1):
    _fr, _to = [int(x) for x in input().split()]
    _fr, _to = _fr - 1, _to - 1
    V[_fr].append(_to)
    V[_to].append(_fr)

def dfs0(root, g, dp, size):
    stack = [(root, -1)]
    post_order = []
    # first pass to determine the order of processing(post-order)
    while stack:
        node, par = stack.pop()
        post_order.append((node, par))
        for nb in g[node]:
            if nb != par:
                stack.append((nb, node))

    # second pass to calculate size and dp value in post-order
    for node, par in reversed(post_order):
        size[node] = 1
        dp[node] = 0
        for nb in g[node]:
            if nb != par:
                size[node] += size[nb]
                dp[node] += dp[nb] + size[nb]

def reroot(fr, to, dp, size):
    dp[fr] -= size[to] + dp[to]
    size[fr] -= size[to]

    size[to] += size[fr]
    dp[to] += size[fr] + dp[fr]

def dfs1(root, g, dp, ans, size):
    stack = [(root, -1)]
    visited = set()
    ans[root] = dp[root]
    
    while stack:
        node, par = stack.pop()
        if node not in visited:
            visited.add(node)

            if par != -1:
                reroot(par, node, dp, size)
                ans[node] = dp[node]
                stack.append((node, par))

            for nb in g[node]:
                if nb != par:
                    stack.append((nb, node))
        else:
            reroot(node, par, dp, size)

dp = [0] * N
dist = [0] * N
size = [0] * N

dfs0(0, V, dp, size)

dfs1(0, V, dp, dist, size)

# find max dist
# print(dist, dp, size)
maximum = max(dist)

# output
M = dist.count(maximum)
print(M)
for i, s in enumerate(dist):
    if s == maximum:
        print(i + 1, end=" ")