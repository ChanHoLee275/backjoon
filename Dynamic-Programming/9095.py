hashTable = {1:1, 2:2, 3:4}

def solution(number):
    if number in hashTable.keys():
        return hashTable[number]
    else:
        for i in range(4, number + 1):
            hashTable[i] = hashTable[i-1] + hashTable[i-2] + hashTable[i-3]
    return hashTable[number]

count = int(input())

for i in range(count):
    print(solution(int(input())))