import aocd


def loadData():
    return aocd.get_data(year=2023, day=11).splitlines()


def findEmptyRowsandCols(data):
    empty_rows = [i for i, row in enumerate(data) 
                  if all(x == '.' for x in row)]
    empty_cols = [j for j, col in enumerate(zip(*data))
                  if all(x == '.' for x in col)]
    return empty_rows, empty_cols


def findPoints(data):
    return [(i, j) for i, row in enumerate(data)
             for j, point in enumerate(row)
             if point == '#']


def countSteps(intervening, empty, expansion_factor):
    numIntervening = len(intervening)
    numEmpty = len(set(empty).intersection(intervening))
    numNonEmpty = numIntervening - numEmpty
    return numNonEmpty + expansion_factor * numEmpty


def solve(data, expansion_factor):
    points = findPoints(data)
    empty_rows, empty_cols = findEmptyRowsandCols(data)

    res = 0
    for idx, point1 in enumerate(points[:-1]):
        for point2 in points[idx+1:]:
            row1, row2 = sorted([point1[0], point2[0]])
            col1, col2 = sorted([point1[1], point2[1]])

            interveningRows = list(range(row1, row2))
            interveningCols = list(range(col1, col2))

            res += countSteps(interveningRows,
                              empty_rows, expansion_factor)
            res += countSteps(interveningCols,
                              empty_cols, expansion_factor)

    return res


def part1(data):
    print(f"Part 1: {solve(data, expansion_factor=2)}")


def part2(data):
    print(f"Part 2: {solve(data, expansion_factor=1000000)}")


INPUT = loadData()
part1(INPUT)
part2(INPUT)
