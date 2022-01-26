from types import new_class


def solution(arrays):
    # 전체를 순회하면서 익은 토마토가 있는 좌표를 뽑아낸다.
    queue = []
    number_of_zeros = 0
    answer = 0
    for i in range(len(arrays)):
        for j in range(len(arrays[0])):
            if arrays[i][j] == 1:
                queue.append([i,j])
            elif arrays[i][j] == 0:
                number_of_zeros += 1
    # BFS로 익지 않은 토마토를 익게 하면서, 날짜를 계산한다.
    while len(queue):
        new_queue = []
        for i in queue:
            [x, y] = i
            if x - 1 >= 0 and arrays[x-1][y] == 0:
                new_queue.append([x-1, y])
                arrays[x-1][y] = 1
                number_of_zeros -= 1
            if x + 1 < len(arrays) and arrays[x+1][y] == 0:
                new_queue.append([x+1, y])
                arrays[x+1][y] = 1
                number_of_zeros -= 1
            if y - 1 >= 0 and arrays[x][y-1] == 0:
                new_queue.append([x, y-1])
                arrays[x][y-1] = 1
                number_of_zeros -= 1
            if y + 1 < len(arrays[0]) and arrays[x][y + 1] == 0:
                new_queue.append([x, y+1])
                arrays[x][y+1] = 1
                number_of_zeros -= 1
        queue = new_queue[:]
        if len(queue):
            answer += 1
    
    if number_of_zeros != 0:
        return -1
    else:
        return answer

[N, M] = list(map(int, input().split(' ')))

arrays = []

for i in range(M):
    arrays.append(list(map(int, input().split(' '))))

print(solution(arrays))