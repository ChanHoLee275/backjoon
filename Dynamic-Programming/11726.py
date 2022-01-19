def solution(number):
    hashTable = {1:1, 2:2}
    if number <= 2:
        return hashTable[number]
    else:
        for i in range(3, number + 1):
            hashTable[i] = (hashTable[i-1] + hashTable[i-2]) % 10007
    return hashTable[number]

print(solution(input()))

