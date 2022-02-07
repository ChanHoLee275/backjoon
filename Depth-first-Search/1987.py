def dfs(matrix, target, history, distance, visited):
    [x,y] = target

    if x-1 >= 0 and not (x-1, y) in visited and not matrix[x-1][y] in history:
        new_history = history[:]
        new_history.append(matrix[x-1][y])
        new_visited = visited[:]
        new_visited.append((x-1,y))
        dfs(matrix, [x-1, y], new_history, distance, new_visited)
    
    if y-1 >= 0 and not (x, y-1) in visited and not matrix[x][y-1] in history:
        new_history = history[:]
        new_history.append(matrix[x][y-1])
        new_visited = visited[:]
        new_visited.append((x,y-1))
        dfs(matrix, [x, y-1], new_history, distance, new_visited)

    if x + 1 < len(matrix) and not (x+1, y) in visited and not matrix[x+1][y] in history:
        new_history = history[:]
        new_history.append(matrix[x+1][y])
        new_visited = visited[:]
        new_visited.append((x+1,y))
        dfs(matrix, [x+1, y], new_history, distance, new_visited)

    if y + 1 < len(matrix[0]) and not (x, y+1) in visited and not matrix[x][y+1] in history:
        new_history = history[:]
        new_history.append(matrix[x][y+1])
        new_visited = visited[:]
        new_visited.append((x,y+1))
        dfs(matrix, [x, y+1], new_history, distance, new_visited)

    distance.append(len(history))

    return 

def solution(arrays):
    distance = []
    dfs(arrays, [0,0], [arrays[0][0]], distance, [(0,0)])
    return max(distance)

[R, C] = list(map(int, input().split(' ')))

arrays = [list(input()) for _ in range(R)]

print(solution(arrays))