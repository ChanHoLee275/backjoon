def solution(arrays):
    answer = []
    for i in range(len(arrays)):
        for j in range(len(arrays[0])):
            if arrays[i][j] == 1:
                count = 1
                queue = [[i,j]]
                arrays[i][j] = 0
                while len(queue):
                    new_queue = []
                    for k in queue:
                        [x,y] = k
                        if x - 1 >= 0 and arrays[x - 1][y] == 1:
                            new_queue.append([x-1,y])
                            arrays[x-1][y] = 0
                            count += 1
                        if x + 1 < len(arrays) and arrays[x+1][y] == 1:
                            new_queue.append([x+1, y])
                            arrays[x+1][y] = 0
                            count += 1
                        if y - 1 >= 0 and arrays[x][y-1] == 1:
                            new_queue.append([x,y-1])
                            arrays[x][y-1] = 0
                            count += 1
                        if y + 1 < len(arrays[0]) and arrays[x][y+1] == 1:
                            new_queue.append([x,y+1])
                            arrays[x][y+1] = 0
                            count += 1
                    print(queue)
                    queue = new_queue[:]
                answer.append(count)
    print(len(answer))
    for i in sorted(answer):
        print(i)
    return

N = int(input())

arrays = []
for i in range(N):
    arrays.append(list(map(int, list(input()))))

solution(arrays=arrays)