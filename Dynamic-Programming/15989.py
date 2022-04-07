dp = [0]*10001
dp[1] = 1 # 1
dp[2] = 2 # 1 1 / 2
dp[3] = 3 # 1 1 1 / 1 2 / 3
dp[4] = 4 # 1 1 1 1 / 1 1 2 / 1 3 / 2 2
dp[5] = 5 # 1 1 1 1 1 / 1 1 1 2 / 1 2 2 / 1 1 3 / 2 3


def solution(number):
    if(dp[number] == 0):
        for i in range(1, number + 1):
            if dp[i] == 0:
                dp[i] = dp[i - 1] + (dp[i-2] - dp[i-3])
                if i % 3 == 0:
                    dp[i] += 1
        return dp[number]
    else :
        return dp[number]

count = int(input())
answer = []
for i in range(count):
    target = int(input())
    answer.append(solution(target))

for i in answer:
    print(i)