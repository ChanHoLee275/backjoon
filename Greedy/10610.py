def solution(number):
    digits = list(map(int,list(number)))
    
    if min(digits) != 0 or sum(digits) % 3 != 0:
        return -1
    
    return ''.join(map(str, sorted(digits,reverse=True)))

print(solution(input()))
