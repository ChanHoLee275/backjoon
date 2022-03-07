def solution(N):
    dp = [{0:0, 1: 1, 2:1, 3:1, 4:1, 5:1, 6:1, 7:1, 8:1, 9:1}]
    if N == 1:
        return sum(list(dp[0].values()))
    for i in range(N - 1):
        target = dp[-1]
        new_target = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0}
        for i in range(0, 10):
            count = target[i]
            if i == 0:
                new_target[1] += 1*count
            elif i == 9:
                new_target[8] += 1*count
            else:
                new_target[i-1] += 1*count
                new_target[i+1] += 1*count
        dp.append(new_target)
    return sum(list(dp.pop().values())) % 1000000000

print(solution(int(input())))