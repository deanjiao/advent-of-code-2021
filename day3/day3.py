# PART 1

f = open('input.txt', 'r')

power_consumption = 0
gamma_rate = '0b'
epsilon_rate = '0b'
lines_count = 0
nums = {}

for line in f:
    for i in range(len(line) - 1):
        if i not in nums:
            nums[i] = 0
        nums[i] += int(line[i])
    lines_count += 1

for i in nums:
    if nums[i] > lines_count / 2:
        gamma_rate += '1'
        epsilon_rate += '0'
    else:
        gamma_rate += '0'
        epsilon_rate += '1'

power_consumption = int(gamma_rate,2) * int(epsilon_rate,2)
print(power_consumption)
