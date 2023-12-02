with open('inputs/day01.txt') as f:
    data = f.readlines()

total = 0
for line in data:
    line.strip()
    ints = [c for c in line if c.isnumeric()]
    total += int(ints[0]+ints[-1])

print(f"Part 1: {total}")

str2nums = {
    'one': 'o1e',
    'two': 't2o',
    'three': 't3e',
    'four': 'f4r',
    'five': 'f5e',
    'six': 's6x',
    'seven': 's7n',
    'eight': 'e8t',
    'nine': 'n9e',
    'zero': 'z0o'
}

total = 0
for line in data:
    line.strip()
    for k, v in str2nums.items():
        line = line.replace(k,v)
    ints = [c for c in line if c.isnumeric()]
    total += int(ints[0]+ints[-1])

print(f"Part 2: {total}")

