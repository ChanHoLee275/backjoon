def solution(binary1, binary2):
    answer = 0
    bits1 = list(binary1)
    bits2 = list(binary2)
    filtered_bits1 = []
    filtered_bits2 = []
    sum_bits1 = 0
    sum_bits2 = 0
    while bits1:
        target1 = bits1.pop()
        target2 = bits2.pop()
        if target1 != target2:
            filtered_bits1.append(target1)
            filtered_bits2.append(target2)
            sum_bits1 += int(target1)
            sum_bits2 += int(target2)
    answer += abs(sum_bits1 - sum_bits2)
    if sum_bits1 >= sum_bits2:
        for i in range(len(filtered_bits1)):
            if filtered_bits1[i] == '0' and filtered_bits2[i] == '1':
                answer += 1
    else:
        for i in range(len(filtered_bits2)):
            if filtered_bits1[i] == '1' and filtered_bits2[i] == '0':
                answer += 1
    return str(answer)

count = int(input())
answers = []
for i in range(count):
    [target1, target2] = input().split()
    answers.append(solution(target1, target2))

print('\n'.join(answers))