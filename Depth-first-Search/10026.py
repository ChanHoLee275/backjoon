from collections import deque
import copy

def dfs(arrays):
    answer = 0
    print(arrays)
    for i in range(len(arrays)):
        for j in range(len(arrays[0])):
            if arrays[i][j] != 0:
                answer += 1
                target = arrays[i][j]
                queue = deque([[i,j]])
                while queue:
                    [x, y] = queue.popleft()
                    if x - 1 >= 0 and arrays[x-1][y] == target:
                        queue.append([x-1,y])
                        arrays[x - 1][y] = 0
                    if y - 1 >= 0 and arrays[x][y-1] == target:
                        queue.append([x, y-1])
                        arrays[x][y - 1] = 0
                    if x + 1 < len(arrays) and arrays[x + 1][y] == target:
                        queue.append([x+1, y])
                        arrays[x + 1][y] = 0
                    if y + 1 < len(arrays[0]) and arrays[x][y + 1] == target:
                        queue.append([x, y + 1])
                        arrays[x][y + 1] = 0
    return answer

def solution(arrays):
    
    arrays2 = copy.deepcopy(arrays)

    for i in range(len(arrays2)):
        for j in range(len(arrays2[0])):
            if arrays2[i][j] == 'R':
                arrays2[i][j] = 'G'
    
    count1 = dfs(arrays)
    count2 = dfs(arrays2)

    return str(count1) + ' ' + str(count2)

count = int(input())

arrays = [list(input()) for i in range(count)]

print(solution(arrays))