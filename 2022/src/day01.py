# process command line args
import sys

# get the filename from the command line
filename = sys.argv[1]

# open the file
with open(filename) as f:
    # read the file into a list
    lines = f.readlines()

# convert the list of strings to a list of ints

max_cals = [0]*3
current_elf = 0
for line in lines:
    if line != '\n':
        current_elf += int(line)
    else:
        if current_elf > max_cals[0]:
            max_cals[0] = current_elf
            max_cals.sort()
        current_elf = 0

print(f'Part 1: {max_cals[-1]}')
print(f'Part 2: {sum(max_cals)}')

