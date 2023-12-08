import aocd
import re
from math import lcm


def loadInput():
    data = aocd.get_data(year=2023, day=8).split("\n\n")
    instructions = list(data[0])

    # AAA = (BBB, CCC)
    pattern = r"([A-Z]{3}) = \(([A-Z]{3}), ([A-Z]{3})\)"
    maps = {}

    for line in data[1].split('\n'):
        match = re.match(pattern, line)

        if match is None:
            raise ValueError(f"Invalid line: {line}")

        key = match.group(1)
        l = match.group(2)
        r = match.group(3)
        maps[key] = (l, r)

    return instructions, maps


def calcNumSteps(instructions, maps, curr, condition):
    i = 0
    while condition(curr):
        instruction = instructions[i % len(instructions)]
        if instruction == 'L':
            curr = maps[curr][0]
        elif instruction == 'R':
            curr = maps[curr][1]
        i += 1
    return i


def part1(instructions, maps):
    curr = "AAA"
    steps = calcNumSteps(instructions, maps, curr, lambda x: x != 'ZZZ')
    print(f"Part 1: {steps}")


def part2(instructions, maps):
    curr = [key for key in maps.keys() if key[-1] == 'A']
    steps = [calcNumSteps(
        instructions, maps, node, lambda x: x[-1] != 'Z') for node in curr]
    print(f"Part 2: {lcm(*steps)}")


INPUT = loadInput()
part1(*INPUT)
part2(*INPUT)
