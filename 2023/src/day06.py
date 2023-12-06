import aocd
import math


def loadInput():
    data = aocd.get_data().split("\n")
    times = [int(x) for x in data[0].split()[1:]]
    distances = [int(x) for x in data[1].split()[1:]]
    return times, distances


def calcNumSuccessful(T, D):
    discriminant = T * T - 4 * D

    # Discriminant always >= 0 in the problem set
    top = math.ceil(0.5 * (-T + math.sqrt(discriminant)))
    bot = math.floor(0.5 * (-T - math.sqrt(discriminant)))

    return top - bot - 1


def part1(times, distances):
    num_successful = []
    for time, distance in zip(times, distances):
        num_successful.append(calcNumSuccessful(time, distance))

    print(f"Part 1: {math.prod(num_successful)}")


def part2(times, distances):
    T = int("".join(map(str, times)))
    D = int("".join(map(str, distances)))

    print(f"Part 2: {calcNumSuccessful(T, D)}")


input = loadInput()

part1(*input)
part2(*input)
