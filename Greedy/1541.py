def sumOfNumbers(chunk):
    return sum(list(map(int,chunk.split('+'))))

def solution(formula):
    answer = 0
    chuncks = formula.split('-')
    first_chunck = chuncks.pop(0)
    answer += sumOfNumbers(first_chunck)
    for i in chuncks:
        answer -= sumOfNumbers(i)
    return answer

print(solution(input()))