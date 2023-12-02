import re
from math import prod

with open('inputs/day02.txt') as f:
    data = f.readlines()


max_vals = {'red': 12, 'green': 13, 'blue': 14}
vals = {'red': 0, 'green': 0, 'blue': 0}

total = 0
sum_powers = 0
for i, line in enumerate(data):
    id = i + 1

    for colour in vals.keys():
        vals[colour] = max(int(num) for num in re.findall(rf'(\d+) {colour}', line))
    
    if all(vals[colour] <= max_vals[colour] for colour in vals.keys()):
        total += id

    sum_powers += prod(vals.values())
    
print(f'Part 1: {total}')
print(f'Part 2: {sum_powers}')