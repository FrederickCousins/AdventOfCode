import aocd


def loadInput():
    data = aocd.get_data(year=2022, day=9).splitlines()
    data = [(line[0], int(line[1]))
            for line in (line.split() for line in data)]
    return data


def updateVisited(rope_loc, visited):
    visited[rope_loc[-1][0]][rope_loc[-1][1]] = True


def updateTailLocs(rope_loc):
    for i in range(1, len(rope_loc)):
        head_loc = rope_loc[i-1]
        tail_loc = rope_loc[i]

        dx = head_loc[1] - tail_loc[1]
        dy = head_loc[0] - tail_loc[0]

        if abs(dx) > 1 or abs(dy) > 1:
            if dx == 0:  # ie same col
                tail_loc[0] += (1 if dy > 0 else -1)
            elif dy == 0:  # ie same row
                tail_loc[1] += (1 if dx > 0 else -1)
            else:  # different row and column
                tail_loc[0] += (1 if dy > 0 else -1)
                tail_loc[1] += (1 if dx > 0 else -1)


def enactInstruction(dir, rope_loc):
    if dir == 'R':
        rope_loc[0][1] += 1
    elif dir == 'D':
        rope_loc[0][0] += 1
    elif dir == 'L':
        rope_loc[0][1] -= 1
    elif dir == 'U':
        rope_loc[0][0] -= 1
    updateTailLocs(rope_loc)


def printGrid(visited, rope_loc, padding=10):
    min_i = max(min(loc[0] for loc in rope_loc) - padding, 0)
    max_i = min(max(loc[0] for loc in rope_loc) + padding, len(visited) - 1)
    min_j = max(min(loc[1] for loc in rope_loc) - padding, 0)
    max_j = min(max(loc[1] for loc in rope_loc) + padding, len(visited[0]) - 1)

    for i in range(min_i, max_i + 1):
        for j in range(min_j, max_j + 1):
            if [i, j] == rope_loc[0]:
                print('H', end='')
            elif [i, j] in rope_loc[1:]:
                print(rope_loc.index([i, j]) - 1, end='')
            elif visited[i][j]:
                print('#', end='')
            else:
                print('.', end='')
        print()
    print()


def part1(data):
    visited = [[False for _ in range(400)] for _ in range(400)]
    rope_loc = [[200, 200] for _ in range(2)]
    updateVisited(rope_loc, visited)

    for dir, steps in data:
        # print(dir, steps)
        for _ in range(steps):
            enactInstruction(dir, rope_loc)
            updateVisited(rope_loc, visited)
        # printGrid(visited, rope_loc)

    total = sum(sum(row) for row in visited)
    print(f"Part 1: {total}")


def part2(data):
    visited = [[False for _ in range(400)] for _ in range(400)]
    rope_loc = [[200, 200] for _ in range(10)]

    updateVisited(rope_loc, visited)

    for dir, steps in data:
        # print(dir, steps)
        for _ in range(steps):
            enactInstruction(dir, rope_loc)
            updateVisited(rope_loc, visited)
        # printGrid(visited, rope_loc)

    total = sum(sum(row) for row in visited)
    print(f"Part 2: {total}")


INPUT = loadInput()
part1(INPUT)
part2(INPUT)
