def solution(count):
    if count == M:
        print(*arr)
        return
    for i in range(N):
        if visited[i] == 0:
            visited[i] = 1
            arr.append(i+1)
            solution(count + 1)
            arr.pop()
            for j in range(i+1, N):
                visited[j] = 0

[N, M] = list(map(int, input().split(' ')))
visited = [0 for _ in range(N)]
arr = []
solution(0)