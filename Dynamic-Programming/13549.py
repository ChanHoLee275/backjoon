def solution(N, K):
    # 걷기는 1초 순간이동은 0초
    roads = [0]*100001
    for i in range(N):
        roads[i] = N - i
    for i in range(N + 1, K + 1):
        if i % 2 == 0:
            target = []
            if i - 1 >= 0:
                target.append(roads[i-1] + 1)
            if i // 2 != 0:
                target.append(roads[i//2])
            roads[i] = min(target)
        else:
            target = []
            if i - 1 >= 0:
                target.append(roads[i-1] + 1)
            if i + 1 <= 100000 and (i + 1) // 2 != 0:
                target.append(roads[(i+1)//2] + 1)
            roads[i] = min(target)
    return roads[K]
[N, K] = list(map(int, input().split()))
print(solution(N, K))