def calc_amount(array, height):
	amount = list(map(lambda x: x - height if x - height > 0 else 0 , array))
	return sum(amount)

def solution(array, limit):
	maximum = max(array)
	minimum = 1
	while minimum <= maximum:
		target = (maximum + minimum) // 2
		amount_tree = calc_amount(array, target)
		if amount_tree >= limit:
			minimum = target + 1
		else:
			maximum = target - 1
	return maximum
	

[N, limit] = list(map(int, input().split(' ')))

target = list(map(int, input().split(' ')))

print(solution(target, limit))

