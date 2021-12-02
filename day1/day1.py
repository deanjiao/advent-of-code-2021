f = open('day1/input.txt', 'r')
last = int(f.readline())
increase_count = 0
for line in f:
    num = int(line)
    if num > last:
        increase_count += 1
    last = num

print(increase_count)