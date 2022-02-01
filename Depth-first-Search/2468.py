from collections import deque


def solution(arrays):
    
    answer = [1]
    maximum = 0
    
    for i in arrays:
        target = i[:]
        target.append(maximum)
        maximum = max(target)
    
    for i in range(1, maximum):
        target = make_island(arrays, i)
        answer.append(find_island(target))
    return max(answer)

def make_island(arrays, target):
    answer = []
    for i in range(len(arrays)):
        answer.append([])
        for j in range(len(arrays[0])):
            if arrays[i][j] > target:
                answer[i].append(arrays[i][j])
            else:
                answer[i].append(0)
    return answer

def find_island(arrays):
    count = 0
    for i in range(len(arrays)):
        for j in range(len(arrays[0])):
            if arrays[i][j] != 0:
                count += 1
                arrays[i][j] = 0
                queue = deque([[i,j]])
                while queue:
                    [x, y] = queue.popleft()
                    if x - 1 >= 0 and arrays[x-1][y] != 0:
                        arrays[x-1][y] = 0
                        queue.append([x-1,y])
                    if y - 1 >= 0 and arrays[x][y-1] != 0:
                        arrays[x][y-1] = 0
                        queue.append([x,y-1])
                    if x + 1 < len(arrays) and arrays[x+1][y] != 0:
                        arrays[x+1][y] = 0
                        queue.append([x+1 ,y])
                    if y + 1 < len(arrays[0]) and arrays[x][y+1] != 0:
                        arrays[x][y+1] = 0
                        queue.append([x, y + 1])
    return count

N = int(input())

arrays = [list(map(int, input().split(' '))) for _ in range(N)]

print(solution(arrays))
