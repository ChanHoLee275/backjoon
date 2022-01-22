def solution(number):
    target = int(number)
    hashTable = {1:0, 2:1, 3:1, 4:2, 5:3, 6:2, 7:3, 8:3, 9:2, 10:3}
    if(target <= 10):
        return hashTable[target]
    for i in range(11, target + 1):
        candidate = []
        if i % 3 == 0 and i % 2 == 0:
            candidate.append(hashTable[i//3] + 1)
            candidate.append(hashTable[i//2] + 1)
            candidate.append(hashTable[i - 1] + 1)
        elif i % 3 == 0:
            candidate.append(hashTable[i//3] + 1)
            candidate.append(hashTable[i - 1] + 1)
        elif i % 2 == 0:
            candidate.append(hashTable[i//2] + 1)
            candidate.append(hashTable[i - 1] + 1)
        else:
            candidate.append(hashTable[i - 1] + 1)
        hashTable[i] = min(candidate)
    return hashTable[target]

print(solution(input()))