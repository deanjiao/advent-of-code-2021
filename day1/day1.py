# PART 1

f = open('day1/input.txt', 'r')
last = int(f.readline())
increase_count = 0
for line in f:
    num = int(line)
    if num > last:
        increase_count += 1
    last = num

print(increase_count)

# PART 2

f = open('day1/input.txt', 'r')
window = []
window.append(int(f.readline()))
window.append(int(f.readline()))
window.append(int(f.readline()))
last_sum = sum(window)
index = 0
increase_count = 0

for line in f:
    num = int(line)
    window[index] = num
    window_sum = sum(window)
    if window_sum > last_sum:
        increase_count += 1
    last_sum = window_sum

    index += 1
    if index > 2:
        index = 0

print(increase_count)