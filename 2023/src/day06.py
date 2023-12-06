import aocd
from math import prod


def loadInput():
    data = aocd.get_data().split("\n")
    times = [int(x) for x in data[0].split()[1:]]
    distances = [int(x) for x in data[1].split()[1:]]
    return times, distances


def calcDistance(hold_time, total_time):
    return (total_time - hold_time) * hold_time


def part1(times, distances):
    num_successful = []
    for time, distance in zip(times, distances):
        num = 0
        for i in range(time):
            s = calcDistance(i, time)
            if s > distance:
                num += 1
        num_successful.append(num)

    print(f"Part 1: {prod(num_successful)}")


def part2(times, distances):
    time = int("".join(map(str, times)))
    distance = int("".join(map(str, distances)))
    num_successful = 0

    for i in range(time):
        s = calcDistance(i, time)
        if s > distance:
            num_successful += 1

    print(f"Part 2: {num_successful}")


input = loadInput()

part1(*input)
part2(*input)
