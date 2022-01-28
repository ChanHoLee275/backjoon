from collections import deque
def solution(person1, person2):
    queue = deque()
    history = [0]*(100000 + 1)
    queue.append(person1)
    while queue:
        target = queue.popleft()
        if target == person2:
            return history[target]
        for i in [target - 1, target + 1, target * 2]:
            if i >= 0 and i <= 100000 and not history[i]:
                history[i] = history[target] + 1
                queue.append(i)


[X, Y] = list(map(int, input().split(' ')))

print(solution(X, Y))