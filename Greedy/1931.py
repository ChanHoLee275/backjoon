count = int(input())
schedule = []

# 회의 입력
for i in range(count):
    schedule.append(list(map( int, input().split(' '))))


sorted_schedule = sorted(schedule, key=lambda conf: (conf[1], conf[0] - conf[1]))

count = 0
end_time = 0

for i in sorted_schedule:
    if end_time <= i[0] :
        end_time = i[1]
        count += 1

print(count)