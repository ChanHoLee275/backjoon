import sys
sys.setrecursionlimit(10**6)

def dfs(idx):
    [x, y] = idx
    if x == 0 and y == 0:
        return 1
    if cache[x][y] == -1:
        cache[x][y] += 1
        if x - 1 >= 0 and maps[x][y] < maps[x - 1][y]:
            cache[x][y] += dfs([x - 1, y])
        if y - 1 >= 0 and maps[x][y] < maps[x][y - 1]:
            cache[x][y] += dfs([x, y - 1])
        if x + 1 < R and maps[x][y] < maps[x + 1][y]:
            cache[x][y] +=  dfs([x + 1, y])
        if y + 1 < C and maps[x][y] < maps[x][y + 1]:
            cache[x][y] += dfs([x, y + 1])
    
    return cache[x][y]

[R, C] = list(map(int, input().split(' ')))
maps = [list(map(int, input().split(' '))) for _ in range(R)]
cache = [[-1]*C for _ in range(R)]
dfs([R-1,C-1])
print(cache[-1][-1])