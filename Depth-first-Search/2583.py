from collections import deque

def solution(arrays):
    answer = []
    for i in range(len(arrays)):
        for j in range(len(arrays[0])):
            if arrays[i][j] == 0:
                count = 1
                queue = deque([[i, j]])
                arrays[i][j] = 1
                while queue:
                    [x, y] = queue.popleft()
                    if x - 1 >= 0 and arrays[x-1][y] == 0:
                        count += 1
                        arrays[x-1][y] = 1
                        queue.append([x-1, y])
                    if y - 1 >= 0 and arrays[x][y-1] == 0:
                        count += 1
                        arrays[x][y-1] = 1
                        queue.append([x,y-1])
                    if x + 1 < len(arrays) and arrays[x+1][y] == 0:
                        count += 1
                        arrays[x+1][y] = 1
                        queue.append([x+1, y])
                    if y + 1 < len(arrays[0]) and arrays[x][y+1] == 0:
                        count += 1
                        arrays[x][y+1] = 1
                        queue.append([x, y+1])
                answer.append(count)
    return sorted(answer)

[M, N, K] = list(map(int, input().split(' ')))

arrays = [[0]*(M) for _ in range(N)]

for _ in range(K):
    [x1, y1, x2, y2] = list(map(int,input().split(' ')))
    for i in range(x1, x2):
        for j in range(y1, y2):
            if arrays[i][j] == 0:
                arrays[i][j] = 1

answer = solution(arrays)
print(len(answer))
print(' '.join(list(map(str, answer))))