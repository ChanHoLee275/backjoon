def solution(arrays, maximum):
    matrix = [[0 for _ in range(maximum + 1)] for _ in range(len(arrays) + 1)]
    for i in range(1,len(arrays) + 1):
        [weight, value] = arrays.pop()
        for j in range(1,maximum + 1):
            if j < weight:
                matrix[i][j] = matrix[i-1][j]
            else:
                matrix[i][j] = max(value + matrix[i-1][j-weight], matrix[i-1][j])
    print(matrix)
    return matrix[-1][-1]


[N, K] = list(map(int,input().split(' ')))

input_arrays = [[0,0]]

for i in range(N):
    input_arrays.append(list(map(int, input().split(' '))))

print(solution(input_arrays, K))