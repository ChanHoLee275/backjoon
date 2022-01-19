price = int(input())
change = 1000 - price
coins = [500, 100, 50, 10, 5, 1]
count = 0

for i in coins:
    count += change // i
    change %= i

print(count)