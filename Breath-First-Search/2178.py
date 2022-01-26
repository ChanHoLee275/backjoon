def solution(arrays, points):
    queue = [[0,0]]
    count = 1
    
    while not points in queue:
        count += 1
        next_queue = []
        for target in queue:
            arrays[target[0]][target[1]] = 0
            if target[0] - 1 >=0 and arrays[target[0]-1][target[1]] == 1:
                next_queue.append([target[0]-1, target[1]])
                arrays[target[0]-1][target[1]] = 0
            if target[0] + 1 < len(arrays) and arrays[target[0] + 1][target[1]] == 1:
                next_queue.append([target[0] + 1, target[1]])
                arrays[target[0] + 1][target[1]] = 0
            if target[1] - 1 >=0 and arrays[target[0]][target[1]-1] == 1:
                next_queue.append([target[0], target[1] - 1])
                arrays[target[0]][target[1] - 1] = 0
            if target[1] + 1 < len(arrays[0]) and arrays[target[0]][target[1] + 1] == 1:
                next_queue.append([target[0], target[1] + 1])
                arrays[target[0]][target[1] + 1] = 0
        queue = next_queue[:]
    return count

[N, M] = list(map(int, input().split(' ')))

arrays = []

for i in range(N):
    arrays.append(list(map(int, list(input()))))

print(solution(arrays, [N - 1, M - 1]))