def marking(queue, arrays):
    new_queue = []
    for i in queue:
        [x,y] = i
        arrays[x][y] = 0
        if x - 1 >= 0 and arrays[x-1][y] == 1:
            arrays[x-1][y] = 0
            new_queue.append([x-1, y])
        if x + 1 < len(arrays) and arrays[x+1][y] == 1:
            arrays[x+1][y] = 0
            new_queue.append([x+1, y])
        if y - 1 >= 0 and arrays[x][y-1] == 1:
            arrays[x][y-1] = 0
            new_queue.append([x, y-1])
        if y + 1 < len(arrays[0]) and arrays[x][y + 1] == 1:
            arrays[x][y+1] = 0
            new_queue.append([x,y+1])
    return new_queue

def solution(arrays):
    count = 0
    for i in range(len(arrays)):
        for j in range(len(arrays[0])):
            if arrays[i][j] == 1:
                queue = [[i,j]]
                arrays[i][j] = 0
                while len(queue):
                    next_queue = marking(queue, arrays)
                    queue = next_queue[:]
                count += 1
    return count

number_of_test = int(input())
answer = []
for i in range(number_of_test):
    [M, N, K] = list(map(int, input().split(' ')))
    arrays = [[0]*N for i in range(M)]
    for i in range(K):
        [x,y] = list(map(int, input().split(' ')))
        arrays[x][y] = 1
    answer.append(solution(arrays))

for i in answer:
    print(i)