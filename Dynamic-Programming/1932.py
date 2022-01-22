def solution(arrays):
    cache = [[0]*len(arrays[-1]) for _ in range(len(arrays[-1]))]
    cache[0][0] = arrays[0][0]
    for i in range(1, len(arrays)):
        target = arrays[i]
        for j in range(len(target)):
            if j > 0 and len(arrays[i-1]) > j:
                cache[i][j] = max(cache[i-1][j-1], cache[i-1][j]) + arrays[i][j]
            elif j > 0:
                cache[i][j] = cache[i-1][j-1] + arrays[i][j]
            else :
                cache[i][j] = cache[i-1][j] + arrays[i][j]
    return max(cache.pop())

count = int(input())
arrays = []
for i in range(count):
    arrays.append(list(map(int, input().split(' '))))

print(solution(arrays))