from collections import deque




length_of_marker = 4
buffer = deque(maxlen=length_of_marker)
count = length_of_marker
with open('2022/inputs/day06.txt') as f:
    buffer.extend(f.read(length_of_marker))
    # print(buffer)
    
    while True:
        char = f.read(1)
        if not char: break
        # print(char)
        # print(list(buffer))
        
        if len(set(buffer)) == length_of_marker:
            break
        else:
            buffer.append(char)
        count += 1


print(f'Part 1: {count}')

length_of_marker = 14
buffer = deque(maxlen=length_of_marker)
count = length_of_marker
with open('2022/inputs/day06.txt') as f:
    buffer.extend(f.read(length_of_marker))
    # print(buffer)
    
    while True:
        char = f.read(1)
        if not char: break
        # print(char)
        # print(list(buffer))
        
        if len(set(buffer)) == length_of_marker:
            break
        else:
            buffer.append(char)
        count += 1

print(f'Part 2: {count}')

    