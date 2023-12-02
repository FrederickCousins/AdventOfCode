import sys

# get the input filename from the command line
filename = sys.argv[1]


with open(filename) as f:
    # read the file into a matrix
    grid = [[int(char) for char in line.strip()] for line in f]

for row in grid:
    print(row)

# Initialize max_from_* lists
max_from_top = [list(row) for row in grid]
max_from_bottom = [list(row) for row in grid]
max_from_left = [list(row) for row in grid]
max_from_right = [list(row) for row in grid]

# Update max_from_top and max_from_left
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if i > 0:
            max_from_top[i][j] = max(max_from_top[i-1][j], grid[i][j])
        if j > 0:
            max_from_left[i][j] = max(max_from_left[i][j-1], grid[i][j])

# Update max_from_bottom and max_from_right
for i in range(len(grid)-1, -1, -1):
    for j in range(len(grid[0])-1, -1, -1):
        if i < len(grid)-1:
            max_from_bottom[i][j] = max(max_from_bottom[i+1][j], grid[i][j])
        if j < len(grid[0])-1:
            max_from_right[i][j] = max(max_from_right[i][j+1], grid[i][j])

# Check if each cell is visible from the edge
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] < min(max_from_top[i][j], max_from_bottom[i][j], max_from_left[i][j], max_from_right[i][j]):
            # The cell is not visible from the edge
            print(f'i,j = {i},{j} is invisible')
            

for row in max_from_top:
    print(row)