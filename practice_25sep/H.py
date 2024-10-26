N = int(input())

grid = []
for i in range(N):
    grid.append(input())

total = 0
for i in range(N):
    total += grid[i].count('1')

horizon = False
for i in range(N):
    rowCount = grid[i].count('1')
    # (N - rowCount) + total - rowCount <= N 
    if total - 2 * rowCount <= 0:
        horizon = True
        break

vertical = False
for j in range(N):
    colCount = 0
    for i in range(N):
        colCount += 1 if grid[i][j] == '1' else 0;
    # (N - rowCount) + total - rowCount <= N 
    if total - 2 * colCount <= 0:
        vertical = True
        break

if horizon and vertical:
    print('+')
elif horizon:
    print('-')
elif vertical:
    print('|')
