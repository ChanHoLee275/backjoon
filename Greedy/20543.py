import sys


def solution(array, M):
    answer = [[0]*len(array[0]) for _ in range(len(array))]
    idx = M // 2
    for i in range(idx, len(array) - idx):
        for j in range(idx, len(array[0]) - idx):
            answer[i][j] = array[i - idx][j-idx]
            if i - idx - 1 >= 0:
                answer[i][j] -= array[i - idx - 1][j - idx]
            if j - idx - 1 >= 0:
                answer[i][j] -= array[i - idx][j - idx - 1]
            if i - idx - 1 >= 0 and j - idx - 1 >= 0:
                answer[i][j] += array[i - idx - 1][j - idx - 1]
            if i - M >= 0:
                answer[i][j] += answer[i - M][j]
            if j - M >= 0:
                answer[i][j] += answer[i][j-M]
            if i - M >= 0 and j - M >= 0:
                answer[i][j] -= answer[i-M][j-M]
    return '\n'.join([' '.join(list(map(lambda x: str(int(abs(x))),i))) for i in answer])

[N, M] = list(map(int, input().split()))

maps = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
print(solution(maps, M))