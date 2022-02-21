def solution(arrays, target):
    hash_table = [0 for i in range(target + 1)]
    hash_table[0] = 1
    for i in arrays:
        for j in range(1, target + 1):
            if j - i >= 0 :
                hash_table[j] += hash_table[j-i]
    return hash_table[target]

[N, K] = list(map(int, input().split(' ')))
numbers = [int(input()) for _ in range(N)]
print(solution(numbers, K))