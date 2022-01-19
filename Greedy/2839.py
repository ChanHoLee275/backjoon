amount = int(input())

count = 0

while amount >= 0:
    if amount % 5 == 0:
        count += amount // 5 
        print(count)
        break
    amount -= 3
    count += 1 
else:
    print(-1)