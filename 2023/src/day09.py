import aocd


def loadInput():
    data = aocd.get_data(year=2023, day=9).split("\n")
    data = [[int(x) for x in line.split()] for line in data]
    return data


def solve(data):
    res = 0
    for line in data:
        diffs = [line]

        i = 0
        while any(x != 0 for x in diffs[i]):
            new_line = [diffs[i][j+1] - diffs[i][j]
                        for j in range(len(diffs[i]) - 1)]
            diffs.append(new_line)
            i += 1

        diffs[-1].append(0)
        for j in range(i-1, -1, -1):
            new_val = diffs[j][-1] + diffs[j+1][-1]
            diffs[j].append(new_val)

        res += diffs[0][-1]

    return res


def part1(data):
    print(f"Part 1: {solve(data)}")


def part2(data):
    data = [line[::-1] for line in data]
    print(f"Part 2: {solve(data)}")


INPUT = loadInput()
part1(INPUT)
part2(INPUT)
