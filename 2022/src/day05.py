import re
from collections import deque
import timeit

start_time = timeit.default_timer()
# Create initial stacks
stacks = [deque() for _ in range(9)]
with open('2022/inputs/day05_1.txt') as f:
    for line in f:
        for i in range(0,36,4):
            element = line[i:i+4].strip('[ ]\n')

            if element:
                stacks[i//4].appendleft(element)

# Process moves
with open('2022/inputs/day05_2.txt') as f:
    for line in f:
        # format: move 4 from 9 to 6
        move_steps = re.search(r'move (\d+) from (\d+) to (\d+)', line)
        if move_steps:
            num, stack1, stack2 = map(int, move_steps.groups())
            # correct off by 1 error
            stack1, stack2 = stack1-1, stack2-1

            for i in range(num):
                stacks[stack2].append(stacks[stack1].pop())

end_time = timeit.default_timer()

print('Time: ', end_time - start_time)

print('Part 1: ',end='')
for stack in stacks:
    print(stack[-1],end='')

print()

## PART 2 

# Recreate initial stacks
stacks = [deque() for _ in range(9)]
with open('2022/inputs/day05_1.txt') as f:
    for line in f:
        for i in range(0,36,4):
            element = line[i:i+4].strip('[ ]\n')

            if element:
                stacks[i//4].appendleft(element)

# Process moves
with open('2022/inputs/day05_2.txt') as f:
    for line in f:
        # format: move 4 from 9 to 6
        move_steps = re.search(r'move (\d+) from (\d+) to (\d+)', line)
        if move_steps:
            num, stack1, stack2 = map(int, move_steps.groups())
            # correct off by 1 error
            stack1, stack2 = stack1-1, stack2-1

            items = [stacks[stack1].pop() for _ in range(num)]

            stacks[stack2].extend(items[::-1])

print('Part 2: ',end='')
for stack in stacks:
    print(stack[-1],end='')

print()