command = list(map(int, input().split(" ")))

types = []
count = 0
money = command[1]
for i in range(command[0]):
    types.append(int(input()))

types.reverse()
for i in types:
    if i <=  money:
        count += money // i
        money %= i
    if(money == 0):
        break
print(count)