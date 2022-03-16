[N, M] = list(map(int, input().split()))
if N == 0:
	print(0)
else :
	books = list(map(int, input().split()))

	count = 1
	total = M

	for i in books:
		if total >= i:
			total -= i
		else:
			count += 1
			total = M - i

	print(count)
