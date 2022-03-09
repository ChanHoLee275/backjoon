def solution(N):
    cnt = 0
    target = 666
    while True:
        if '666' in str(target):
            cnt += 1
            if cnt == N:
                return target
        target += 1

print(solution(int(input())))