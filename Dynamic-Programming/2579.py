def solution(numbers):
    if len(numbers) <= 2:
        return sum(numbers)
    cache = [0]*len(numbers)
    cache[0] = numbers[0]
    cache[1] = numbers[0] + numbers[1]
    cache[2] = max(numbers[1] + numbers[2], numbers[0] + numbers[2])
    for i in range(3, len(numbers)):
        cache[i] = max(cache[i - 3] + numbers[i - 1] + numbers[i], cache[i - 2] + numbers[i])
    return cache[len(numbers) - 1]
count = int(input())
numbers = []

for i in range(count):
    numbers.append(int(input()))

print(solution(numbers))