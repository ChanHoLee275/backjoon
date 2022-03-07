def solution(array):
    if len(array) <= 3:
        return sum(array)
    cache = [0, array[1], array[1] + array[2]]
    for i in range(3, len(array)):
        cache.append(max(cache[i-2] + array[i], array[i] + array[i-1] + cache[i-3], cache[i-1]))
    return cache.pop()

count = int(input())
array = [0]
for i in range(count):
    array.append(int(input()))
print(solution(array=array))