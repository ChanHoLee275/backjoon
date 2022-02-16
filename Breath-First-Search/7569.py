import sys

def solution(arrays):
    answer = 0
    the_number_of_one = 0
    the_number_of_minus_one = 0
    total = len(arrays)*len(arrays[0])*len(arrays[0][0])
    
    queue = []

    for i in range(len(arrays)):
        for j in range(len(arrays[0])):
            for k in range(len(arrays[0][0])):
                if arrays[i][j][k] == 1:
                    queue.append([i,j,k])
                    the_number_of_one += 1
                elif arrays[i][j][k] == -1:
                    the_number_of_minus_one += 1
    while queue:
        new_queue = []
        for i in queue:
            [z, y, x] = i
            # 위
            if len(arrays) > z + 1 and arrays[z+1][y][x] == 0:
                arrays[z+1][y][x] = 1
                the_number_of_one += 1
                new_queue.append([z+1, y, x])
            # 아래
            if z - 1 >= 0 and arrays[z-1][y][x] == 0:
                arrays[z-1][y][x] = 1
                the_number_of_one += 1
                new_queue.append([z-1,y,x])
            # 왼쪽
            if x - 1 >= 0 and arrays[z][y][x-1] == 0:
                arrays[z][y][x-1] = 1
                the_number_of_one += 1
                new_queue.append([z, y, x-1])
            # 오른쪽
            if x + 1 < len(arrays[0][0]) and arrays[z][y][x+1] == 0:
                arrays[z][y][x+1] = 1
                the_number_of_one += 1
                new_queue.append([z, y, x+1])
            # 앞
            if y - 1 >= 0 and arrays[z][y-1][x] == 0:
                arrays[z][y-1][x] = 1
                the_number_of_one += 1
                new_queue.append([z, y-1, x])
            # 뒤
            if y + 1 < len(arrays[0]) and arrays[z][y+1][x] == 0:
                arrays[z][y+1][x] = 1
                the_number_of_one += 1
                new_queue.append([z, y+1, x])
        queue = new_queue[:]
        answer += 1

    if the_number_of_minus_one + the_number_of_one == total:
        return answer - 1
    else:
        return -1

[r, c, h] = list(map(int, input().split(' ')))

box = []

for i in range(h):
    layer = []
    for j in range(c):
        layer.append(list(map(int, sys.stdin.readline().split())))
    box.append(layer)

print(solution(box))