import sys
def solution(array):
    answer = 1
    sorted_array = sorted(array)
    min_score = sorted_array[0][1]
    for i in range(1, len(sorted_array)):
        if sorted_array[i][1] < min_score:
            answer += 1
            min_score = sorted_array[i][1]
    return answer

count = int(input())

target = []

for i in range(count):
    queue = []
    iter = int(input())
    for j in range(iter):
        queue.append(list(map(int, sys.stdin.readline().split())))
    target.append(queue)

for i in target:
    print(solution(i))