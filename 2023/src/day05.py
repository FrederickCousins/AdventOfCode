
def loadInput(filename: str) -> tuple[list, list]:
    sections = open(filename).read().strip().split("\n\n")

    seeds, *sections = sections

    seeds = [int(x) for x in seeds.split(":")[1].split()]

    maps = [[list(map(int, line.split())) 
            for line in m.split("\n")[1:]] 
            for m in sections
    ]

    return seeds, maps


def solve(seed_ranges, maps, DEBUG=False):
    for i, m in enumerate(maps):
        if DEBUG:
            print(f"Layer {i+1}")
            print(seed_ranges)
        new_ranges = []
        while len(seed_ranges) != 0:
            # print(f"Start of loop, seed_ranges are: \n {seed_ranges}","\n\n")
            range_start, range_end = seed_ranges.pop(0)
            # print(f"Processing input range: ({range_start}, {range_end})")
            processed = False

            for dest_start, source_start, map_length in m:
                source_end = source_start + map_length
                dest_end = dest_start + map_length
                shift = dest_start - source_start

                # ENDS ARE EXCLUSIVE
                # IE (56,60) -> 56,57,58,59

                # SIX CASES FOR EACH MAP:
                if range_end <= source_start or source_end <= range_start:
                    # |<range>|  or       |<range>|
                    #         |<---map--->|
                    continue

                elif range_start < source_start < range_end <= source_end:
                    # |<range>|
                    #      |<---map--->|
                    seed_ranges.append((range_start, source_start))
                    new_ranges.append((dest_start, range_end + shift))
                    processed = True

                elif range_start < source_start < source_end < range_end:
                    # |<--------range------->|
                    #      |<---map--->|
                    seed_ranges.append((range_start, source_start))
                    seed_ranges.append((source_end, range_end))
                    new_ranges.append((dest_start, dest_end))
                    processed = True

                elif source_start <= range_start < range_end <= source_end:
                    #        |<-range->|
                    #        |<--map-->|
                    new_ranges.append((range_start + shift, range_end + shift))
                    processed = True

                elif source_start <= range_start < source_end < range_end:
                    #          |<----range-->|
                    #      |<---map--->|
                    seed_ranges.append((source_end, range_end))
                    new_ranges.append((range_start + shift, dest_end))
                    processed = True

            # In case none of the maps have any overlap
            if not processed:
                new_ranges.append((range_start, range_end))

        # When all ranges have been processed (stack empty)
        seed_ranges = list(set(new_ranges.copy()))
        seed_ranges.sort()

    return min([x for x, _ in seed_ranges])


def part1(input):
    seeds, maps = input
    locations = []

    seed_ranges = [(x, x + 1) for x in seeds]

    print(f"Part 1: {solve(seed_ranges, maps)}")


def part2(input):
    seeds, maps = input

    seed_ranges = [(x, x + y) for x, y in zip(seeds[::2], seeds[1::2])]

    print(f"Part 2: {solve(seed_ranges, maps)}")


input = loadInput("2023/inputs/day05.txt")

part1(input)
part2(input)
