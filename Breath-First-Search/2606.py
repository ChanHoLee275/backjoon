def solution(arrays):
    count = 0
    queue = [0]
    infected = set()
    while len(queue):
        new_queue = []
        for i in queue:
            target = arrays[i]
            for j in range(len(target)):
                if arrays[i][j] == 1 and not (i in infected and j in infected):
                    new_queue.append(j)
                    arrays[i][j] = 0
                    arrays[j][i] = 0
                    infected.add(j)
                    infected.add(i)
                    count += 1
        queue = new_queue[:]
    return count

N = int(input())

arrays = [[0]*N for i in range(N)]

M = int(input())

for i in range(M):
    inputs = list(map(int, input().split(' ')))
    arrays[inputs[0]-1][inputs[1]-1] = 1
    arrays[inputs[1]-1][inputs[0]-1] = 1

print(solution(arrays))            