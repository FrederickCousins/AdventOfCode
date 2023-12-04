import re
from collections import defaultdict

with open("2023/inputs/day04.txt", encoding="utf-8") as f:
    data = f.readlines()

pattern = r"Card\s+(\d+):\s+((?:\d+\s*)+)\|\s+((?:\d+\s*)+)"

res1 = 0
part2dict = defaultdict(int)
for line in data:
    line = line.strip()

    match = re.match(pattern, line)

    if match:
        card_id = int(match.group(1))
        winning_nums = list(map(int, match.group(2).split()))
        elfs_nums = list(map(int, match.group(3).split()))

        # print(line)
        # print("Card ID:", card_id)
        # print("List 1:", winning_nums)
        # print("List 2:", elfs_nums)

    else:
        # print("No match")
        break

    num_common_elements = len(set(winning_nums) & set(elfs_nums))

    if num_common_elements > 0:
        res1 += 2 ** (num_common_elements - 1)

    part2dict[card_id] += 1
    for i in range(num_common_elements):
        part2dict[card_id + 1 + i] += part2dict[card_id]


print(f"Part 1: {res1}")

res2 = sum(part2dict.values())

print(f"Part 2: {res2}")

print(part2dict)
