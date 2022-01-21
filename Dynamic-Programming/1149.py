def solution(candidates):
    for i in range(1, len(candidates)):
        candidates[i][0] = min(candidates[i - 1][1], candidates[i - 1][2]) + candidates[i][0]
        candidates[i][1] = min(candidates[i - 1][0], candidates[i - 1][2]) + candidates[i][1]
        candidates[i][2] = min(candidates[i - 1][0], candidates[i - 1][1]) + candidates[i][2]
    return min(candidates.pop())

count = int(input())
candidate = []

for i in range(count):
    candidate.append(list(map(int,input().split(' '))))

print(solution(candidate))
