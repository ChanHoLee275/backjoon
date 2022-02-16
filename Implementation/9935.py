import re

# 정규 표현식 풀이
def solution(string, target):
    start_string = string
    next_string = re.sub(target, '', start_string)      
    while start_string != next_string:
        start_string = next_string
        next_string = re.sub(target, '', start_string)
    if next_string != '':
        return next_string
    else:
        return 'FRULA'

# 스택 풀이
def solution2(string, target):
    chars = list(string)
    bomb = list(target)
    stack = []
    for i in chars:
       stack.append(i)
       if i == bomb[-1] and ''.join(stack[-len(bomb):]) == target:
           del stack[-len(bomb):]
    if len(stack) == 0:
        return 'FRULA'
    else:
        return ''.join(stack)

strings = input()
target = input()

print(solution2(strings, target))