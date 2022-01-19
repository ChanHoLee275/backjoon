count = int(input())
ropes = []

for i in range(count):
    ropes.append(int(input()))

ropes.sort(reverse=True)

for idx, value in enumerate(ropes):
    ropes[idx] = value*(idx + 1)

print(max(ropes))

# edge case : count: 6, input: 4, 1, 1, 1, 1, 1