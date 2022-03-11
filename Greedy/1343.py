def solution(strings, original):
    answer = ''
    new_strings = []
    for i in strings:
        if len(i) < 2:
            return -1
        else:
            length = len(i)
            tmp = ''
            while length >= 4:
                tmp += 'AAAA'
                length -= 4
            while length >= 2:
                tmp += 'BB'
                length -= 2
            if length != 0:
                return -1
            new_strings.append(tmp)
    new_strings = ''.join(new_strings)
    idx = 0
    for i in range(len(original)):
        if original[i] != '.':
            answer += new_strings[idx]
            idx += 1
        else:
            answer += '.'
    return answer

original_strings = input()
strings = list(filter(lambda x: len(x) > 0, original_strings.split('.')))
print(solution(strings=strings, original=original_strings))