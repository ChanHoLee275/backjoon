def solution(arrays):
    cache = [[0]*len(arrays[0]) for _ in range(len(arrays))]
    cache[0][0] = arrays[0][0]
    cache[1][0] = arrays[1][0]
    if len(arrays[0]) == 1:
        return max(cache[0][0], cache[1][0])
    cache[0][1] = cache[1][0] + arrays[0][1]
    cache[1][1] = cache[0][0] + arrays[1][1]
    for i in range(2, len(arrays[0])):
        cache[0][i] = max(arrays[0][i] + cache[1][i-1], arrays[0][i] + cache[0][i-2], arrays[0][i] + cache[1][i-2])
        cache[1][i] = max(arrays[1][i] + cache[0][i-1], arrays[1][i] + cache[1][i-2], arrays[1][i] + cache[0][i-2])
    return max(cache[0][-1], cache[1][-1])

count = int(input())

for i in range(count):
    column = int(input())
    arrays = []
    for i in range(2):
        arrays.append(list(map(int, input().split(' '))))
    print(solution(arrays=arrays))