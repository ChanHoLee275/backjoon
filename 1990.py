def isPrime(number):
    for i in range(2,int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

def isPalindrome(number):
    target = list(str(number))
    return True if target == target[::-1] else False
    

[start, end] = list(map(int ,input().split()))

if end > 10000000:
    end = 10000000

candidates = range(start, end+1)

answers = filter(isPrime, filter(isPalindrome, candidates))

for i in answers:
    print(i)
print(-1)