def solution(arrays):
    distances = [0]*len(arrays)
    distances[0] = 1
    for i in range(1, len(arrays)):
        candidates = []
        for j in range(i - 1,-1, -1):
            if arrays[i] > arrays[j]:
                candidates.append(distances[j])
        if len(candidates) != 0:
            distances[i] = max(candidates) + 1
        else:
            distances[i] = 1
    return max(distances)

count = int(input())
print(solution(list(map(int, input().split(' ')))))