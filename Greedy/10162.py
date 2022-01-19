def divideByTime(target, time):
    return [target//time, target % time]

A = 300
B = 60
C = 10

target = int(input())

[count_A, target] = divideByTime(target, A)
[count_B, target] = divideByTime(target, B)
[count_C, target] = divideByTime(target, C)

if target != 0:
    print(-1)
else:
    print(str(count_A), str(count_B), str(count_C))
