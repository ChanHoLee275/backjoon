count = int(input())

numbers = sorted(list(map(int, input().split(" "))))
acc = [numbers[0]]

for i in range(len(numbers)-1):
	acc.append(acc[-1] + numbers[i+1])
print(sum(acc))