# open the file
with open('2022/inputs/day03.txt') as f:
    # read the file into a list of lines
    lines = f.readlines()

# create a dictionary for priorities
# Create character ranges
lowercase_chars = [chr(i) for i in range(ord('a'), ord('z')+1)]
uppercase_chars = [chr(i) for i in range(ord('A'), ord('Z')+1)]

# Create dictionary char: priority
priorities = {char: ord(char) - 96 if char.islower() else ord(char) - 38 for char in lowercase_chars + uppercase_chars}
# print(priorities)

score = 0
for line in lines:
    length = len(line.strip('\n'))
    compartment_size = length // 2

    l1 = set(line[:compartment_size])
    l2 = set(line[compartment_size:-1])

    common = l1 & l2

    score += sum([priorities[char] for char in common])

print(f'Part 1: {score}')

# Part 2
score = 0
for i in range(0, len(lines), 3):
    l1 = set(lines[i].strip('\n'))
    l2 = set(lines[i+1].strip('\n'))
    l3 = set(lines[i+2].strip('\n'))  

    common = l1 & l2 & l3

    score += sum([priorities[char] for char in common])

print(f'Part 2: {score}')
    