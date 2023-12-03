from math import prod

with open('2023/inputs/day03.txt') as f:
    data = [[char if char != '.' else '' for char in line.strip()] for line in f]

def checkAreaForSymbol(i, j, length) -> bool:
    '''i, j are the indicies of the last digit of a number which has length''' 
    l = max(0, j - length)
    r = min(len(data[i]), j+2)

    above = data[i-1][l:r] if i > 0 else []
    below = data[i+1][l:r] if i < len(data) - 1 else []
   
    left = data[i][j-length] if j - length >= 0 else ''
    right = data[i][j+1] if j+1 < len(data[i]) - 1 else ''
    
    # print(f'tmp: {tmp}, above: {above}, below: {below}, left: {left}, right: {right}\n')
    
    if above and any(c and not c.isnumeric() for c in above) or \
       below and any(c and not c.isnumeric() for c in below) or \
       left and not left.isnumeric() or \
       right and not right.isnumeric():
        return True
    else:
        return False
    
res = 0
for i, row in enumerate(data):
    tmp = ''
    for j, k in enumerate(row):
        if k.isnumeric(): # add k to tmp
            tmp += k
                
        # There are two cases for clearing tmp
        # 1. We are at the end of current row
        # 2. The next element is not numeric
        if tmp and (j == len(row) - 1 or not row[j+1].isnumeric()):
            if checkAreaForSymbol(i, j, len(tmp)):
                res += int(tmp)
            tmp = ''
            
print(f'Part 1: {res}')

def extractNumsAroundGear(i,j):
    nums = []
    box = [[x for x in r[j-1:j+2]] for r in data[i-1:i+2]]
    box[1][1] = ''

    # for r in box: print(r)
    
    for ii, row in enumerate(box,-1):
        if row[1]:
            tmp = row[1]
            jj = 1
            while data[i + ii][j - jj]:
                tmp = data[i + ii][j - jj] + tmp
                jj += 1
            jj = 1
            while data[i + ii][j + jj]:
                tmp += data[i + ii][j + jj]
                jj += 1
            nums.append(int(tmp))
        else:
            if row[0]:
                tmp = row[0]
                jj = 1
                while data[i + ii][j - 1 - jj]:
                    tmp = data[i + ii][j - 1 - jj] + tmp
                    jj += 1
                nums.append(int(tmp))
            if row[2]:
                tmp = row[2]
                jj = 1
                while data[i + ii][j + 1 + jj]:
                    tmp += data[i + ii][j + 1 + jj]
                    jj += 1
                nums.append(int(tmp))
    
    return nums

res = 0
for i, row in enumerate(data):
    tmp = ''
    for j, k in enumerate(row):
        if k == '*':
            nums = extractNumsAroundGear(i,j)
            
            # print(nums, '\n')

            if len(nums) == 2:
                res += prod(nums)

print(f'Part 2: {res}')
