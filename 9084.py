import sys
read = sys.stdin.readline

T = int(read())

for i in range(T):
    N = int(read())
    coins = list(map(int, read().split()))
    M = int(read())
    dp = [0 for _ in range(M + 1)]
    dp[0] = 1
    for i in range(N):
        # coins[i]에 대해서 이보다 큰 금액은 이 코인과 다른 코인들의 합으로 표현할 수 있다.
        for j in range(coins[i], M + 1):
            dp[j] += dp[j - coins[i]]
    print(dp[M])