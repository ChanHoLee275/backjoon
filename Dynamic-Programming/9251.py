def solution(string1, string2):
    memory = [[0]*(len(string2) + 1) for _ in range(len(string1) + 1)]
    for i in range(1, len(string1) + 1):
        for j in range(1, len(string2) + 1):
            if string1[i-1] == string2[j-1]:
                memory[i][j] = memory[i-1][j-1] + 1
            else:
                memory[i][j] = max(memory[i-1][j], memory[i][j-1])
    return memory[-1][-1]

str1 = input()
str2 = input()

print(solution(str1, str2))