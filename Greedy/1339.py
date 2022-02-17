def solution(chars):
    answer = 0
    hash_table = dict()
    for i in chars:
        target = list(i)
        target.reverse()
        for j in range(len(target)):
            if target[j] in list(hash_table.keys()):
                hash_table[target[j]] = hash_table[target[j]] + 10**j
            else:
                hash_table[target[j]] = 10**j
    items = list(map(lambda x: (x[1], x[0]), hash_table.items()))
    items.sort(reverse=True)
    start = 9
    for i in items:
        (value, key) = i
        answer += start*value
        start -= 1
    return answer



count = int(input())
lists = []
for i in range(count):
    lists.append(input())

print(solution(lists))