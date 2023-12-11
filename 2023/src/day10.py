import aocd


DIRS = {'F': [(1, 0), (0, 1)],
        '|': [(1, 0), (-1, 0)],
        '-': [(0, -1), (0, 1)],
        'J': [(0, -1), (-1, 0)],
        'L': [(-1, 0), (0, 1)],
        '7': [(0, -1), (1, 0)]}


def loadInput():
    data = aocd.get_data(year=2023, day=10)
    data = [[char for char in line] for line in data.splitlines()]
    return data


def findStart(data):
    for i, row in enumerate(data):
        for j, element in enumerate(row):
            if element == 'S':
                return (i, j)


def findInitialPaths(data, start_pos):
    i, j = start_pos

    points = []
    if data[i-1][j] in ['|', 'F', '7']:
        points.append((i-1, j))
    if data[i][j-1] in ['-', 'F']:
        points.append((i, j-1))
    if data[i][j+1] in ['-', 'J', '7']:
        points.append((i, j+1))
    if data[i+1][j] in ['|', 'J', 'L']:
        points.append((i+1, j))

    if len(points) != 2:
        print("Error, should be exactly two starting paths")
        return None

    res0 = [(i, j), points[0]]
    res1 = [(i, j), points[1]]

    return res0, res1


def followPath(data, path):
    i, j = path[-1]

    possible = DIRS[data[i][j]]

    for point in possible:
        new_point = (i + point[0], j + point[1])
        if new_point != path[-2]:
            path.append(new_point)
            break


def part1(data):
    start_pos = findStart(data)
    path0, path1 = findInitialPaths(data, start_pos)

    while path0[-1] != path1[-1]:
        followPath(data, path0)
        followPath(data, path1)

    print(f"Part 1: {len(path0)-1}")


def part2(data):
    start_pos = findStart(data)
    path, _ = findInitialPaths(data, start_pos)

    while path[-1] != start_pos:
        followPath(data, path)
    path.pop()

    # Calculate area using shoelace formula
    area = 0
    L = len(path)
    for idx in range(L):
        area += path[idx][0] * path[(idx+1) % L][1]
        area -= path[idx][1] * path[(idx+1) % L][0]
    area = abs(area)/2

    # Pick's Formula to find num interior points
    res = area + 1 - (L/2)

    print(f"Part 2: {int(res)}")


INPUT = loadInput()
part1(INPUT)
part2(INPUT)
