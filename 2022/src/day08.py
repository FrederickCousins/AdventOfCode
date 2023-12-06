import aocd


def loadInput():
    f = aocd.get_data(year=2022, day=8).split("\n")

    grid = [[int(char) for char in line.strip()] for line in f]
    gridT = [[grid[j][i] for j in range(len(grid))] for i in range(len(grid[0]))]
    return grid, gridT


def part1(grid, gridT):
    total = 0
    for i, row in enumerate(grid):
        for j, tree in enumerate(row):
            col = gridT[j]
            above = col[:i]
            left = row[:j]
            below = col[i + 1 :]
            right = row[j + 1 :]
            if (
                all(tree > x for x in above)
                or all(tree > x for x in left)
                or all(tree > x for x in below)
                or all(tree > x for x in right)
            ):
                total += 1

    print(f"Part 1: {total}")


def viewingDistance(height, trees):
    if not trees:
        return 0

    for i, tree in enumerate(trees, 1):
        if tree >= height:
            return i

    return len(trees)


def part2(grid, gridT):
    best = 0
    for i, row in enumerate(grid):
        for j, tree in enumerate(row):
            col = gridT[j]

            above = viewingDistance(tree, col[:i][::-1])
            left = viewingDistance(tree, row[:j][::-1])
            below = viewingDistance(tree, col[i + 1 :])
            right = viewingDistance(tree, row[j + 1 :])

            score = above * left * below * right

            best = max(best, score)

    print(f"Part 2: {best}")


input = loadInput()

part1(*input)
part2(*input)
