from collections import deque
import copy
[N, M] = list(map(int, input().split(' ')))
arr = [list(map(int, input().split(' '))) for _ in range(N)]
ans = 0
dx = [0,0,-1,1] 
dy = [1,-1,0,0]

def bfs():
    global ans
    target = copy.deepcopy(arr)
    queue = deque()
    for i in range(N):
        for j in range(M):
            if target[i][j] == 2:
                queue.append([i,j])
    while queue:
        [x, y] = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if target[nx][ny] == 0:
                    target[nx][ny] = 2
                    queue.append([nx, ny])
    cnt = 0
    for i in target:
        cnt += i.count(0)
    ans = max(ans, cnt)

def wall(x):
    if x == 3:
        bfs()
        return
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 0:
                arr[i][j] = 1
                wall(x + 1)
                arr[i][j] = 0

wall(0)
print(ans)