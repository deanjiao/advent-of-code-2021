# PART 1

f = open('day2/input.txt', 'r')
horizontal = 0
depth = 0

for line in f:
    direction, x = line.split()
    if direction == 'forward':
        horizontal += int(x)
    elif direction == 'down':
        depth += int(x)
    elif direction == 'up':
        depth -= int(x)

result = horizontal * depth
print(result)

# PART 2

f = open('day2/input.txt', 'r')
horizontal = 0
depth = 0
aim = 0

for line in f:
    direction, x = line.split()
    if direction == 'forward':
        horizontal += int(x)
        depth += aim * int(x)
    elif direction == 'down':
        aim += int(x)
    elif direction == 'up':
        aim -= int(x)

result = horizontal * depth
print(result)
