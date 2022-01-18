count = int(input())

target = []

for i in range(2):
    for j in input().split(' '):
        target.append(int(j))

A = sorted(target[0:count])
B = target[count:]

answer = 0

for i in A:
    maximum = max(B)
    answer +=  i * maximum
    idx = B.index(maximum)
    del B[idx]

print(answer)