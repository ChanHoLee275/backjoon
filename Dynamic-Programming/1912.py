def solution(arrays):
    cache = [0]*len(arrays)
    cache[0] = arrays[0]
    for i in range(1,len(arrays)):
        cache[i] = max(cache[i-1] + arrays[i], arrays[i])
    return max(cache)   

count = int(input())

print(solution(list(map(int, input().split(' ')))))