from collections import deque


def bfs(matrix, x, y):
    queue = deque([[x,y]])
    sheep = 0
    wolf = 0
    if matrix[x][y] == 'v':
        wolf += 1
    elif matrix[x][y] == 'k':
        sheep += 1
    matrix[x][y] = '.'
    while(len(queue) != 0):
        [i, j] = queue.popleft()
        target = [[i-1, j],[i, j + 1],[i, j - 1], [i+1, j]]
        for k in target:
            if 0 <= k[0] < len(matrix) and 0<= k[1] < len(matrix[1]) and matrix[k[0]][k[1]] != '#':
                if matrix[k[0]][k[1]] == 'v':
                    wolf += 1
                if matrix[k[0]][k[1]] == 'k':
                    sheep += 1
                matrix[k[0]][k[1]] = '#'
                queue.append([k[0], k[1]])
    if sheep > wolf:
        return [sheep, 0]
    else:
        return [0, wolf]

def solution(matrix):
    sheep = 0
    wolf = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 'k' or matrix[i][j] == 'v':
                [remainSheep, remainWolf] = bfs(matrix, i ,j)
                sheep += remainSheep
                wolf += remainWolf
    return [sheep, wolf]


[R, C] = list(map(int, input().split(' ')))

matrix = []

for i in range(R):
    matrix.append(list(input()))
[sheep, wolf] = solution(matrix=matrix)
print(sheep, wolf)