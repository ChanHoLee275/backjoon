def is_group_word(chars):
    cache = dict()
    for i in range(len(chars)):
        if chars[i] in cache.keys():
            cache[chars[i]].append(i)
        else:
            cache[chars[i]] = [i]
    for i in cache.keys():
        target = cache[i]
        for j in range(len(target) - 1):
            if target[j] + 1 != target[j+1]:
                return False
    return True

def solution(strings):
    answer = 0
    for i in strings:
        if is_group_word(list(i)):
            answer += 1
    return answer

count = int(input())

strings = [input() for _ in range(count)]

print(solution(strings=strings))