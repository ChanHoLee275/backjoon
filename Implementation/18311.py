def solution(arrays, k):
    total_distance = sum(arrays)
    reverse_arrays = list(reversed(arrays[:]))
    if k > total_distance:
        k -= total_distance
        for i in range(len(reverse_arrays)):
            if reverse_arrays[i] > k:
                return len(arrays) - i
            else:
                k -= reverse_arrays[i]
    else:
        for i in range(len(arrays)):
            if arrays[i] > k:
                return i + 1
            else:
                k -= arrays[i]

[count, distance] = list(map(int, input().split(' ')))

arrays = list(map(int, input().split(' ')))

print(solution(arrays=arrays, k=distance))