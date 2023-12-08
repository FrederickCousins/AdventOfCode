import aocd
import re
from math import lcm


def loadInput():
    data = aocd.get_data(year=2023, day=8).split("\n\n")
    instructions = list(data[0])

    maps = {}
    for line in data[1].split('\n'):
        key, l, r = re.findall(r"([A-Z]{3})", line)
        maps[key] = (l, r)

    return instructions, maps


def calcNumSteps(instructions, maps, curr, stop_condition):
    i = 0
    while not stop_condition(curr):
        instruction = instructions[i % len(instructions)]
        curr = maps[curr][instruction == 'R']  # L: 0, R: 1
        i += 1
    return i


def part1(instructions, maps):
    curr = "AAA"
    steps = calcNumSteps(instructions, maps, curr, lambda x: x == 'ZZZ')
    print(f"Part 1: {steps}")


def part2(instructions, maps):
    curr = [key for key in maps.keys() if key.endswith('A')]
    steps = [calcNumSteps(
        instructions, maps, node, lambda x: x.endswith('Z')) for node in curr]
    print(f"Part 2: {lcm(*steps)}")


INPUT = loadInput()
part1(*INPUT)
part2(*INPUT)
