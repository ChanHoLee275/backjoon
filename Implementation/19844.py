import re

def solution(string):
    answer = 0
    regx = re.compile("^(c|j|n|m|t|s|l|d|qu)(')[aeiouh]")
    parts_of_string = re.split("-| ", string)
    for i in parts_of_string:
        if regx.match(i) != None:
            answer += 2
        else:
            answer += 1
    return answer

string = input()

print(solution(string))