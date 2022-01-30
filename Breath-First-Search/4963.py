from collections import deque

def solution(arrays):
    answer = 0
    w = len(arrays)
    h = len(arrays[0])
    for i in range(w):
        for j in range(h):
            if arrays[i][j] == 1:
                arrays[i][j] = 0
                queue = deque([[i, j]])
                while queue:
                    [x, y] = queue.popleft()
                    # TODO: 아래의 코드 압축할 수 있는 방법 찾기
                    if x - 1 >= 0:
                        if arrays[x-1][y] == 1:
                            queue.append([x-1, y])
                            arrays[x-1][y] = 0
                        if y - 1 >= 0 and arrays[x-1][y-1] == 1:
                            queue.append([x-1, y-1])
                            arrays[x-1][y-1] = 0
                        if y + 1 < h and arrays[x-1][y+1] == 1:
                            queue.append([x-1,y+1])
                            arrays[x-1][y+1] = 0
                    if x + 1 < w:
                        if arrays[x+1][y] == 1:
                            queue.append([x+1, y])
                            arrays[x+1][y] = 0
                        if y - 1 >= 0 and arrays[x+1][y-1] == 1:
                            queue.append([x+1, y-1])
                            arrays[x+1][y-1] = 0
                        if y + 1 < h and arrays[x+1][y+1] == 1:
                            queue.append([x+1,y+1])
                            arrays[x+1][y+1] = 0
                    if y - 1 >= 0 and arrays[x][y-1] == 1:
                        queue.append([x, y-1])
                        arrays[x][y-1] = 0
                    if y + 1 < h and arrays[x][y+1] == 1:
                        queue.append([x, y+1])
                        arrays[x][y+1] = 0
                answer += 1
    return answer

command = input()

matrixs = []

while command != '0 0':
    [N, M] = list(map(int, command.split(' ')))
    matrixs.append([list(map(int, input().split(' '))) for _ in range(M)])
    command = input()

for i in list(map(solution, matrixs)):
    print(i)