import re

count1 = 0
count2 = 0
# open the file
with open('2022/inputs/day04.txt') as f:
    for line in f:
        # process line 'num1-num2,num3-num4' using regex
        # print(f"Processing line: {line.strip()}")
        processed = re.search(r'(\d+)-(\d+),(\d+)-(\d+)', line)
        if processed:
            num1, num2, num3, num4 = map(int, processed.groups())
            # print(num1, num2, num3, num4)

            if (num1 <= num3 and num2 >= num4) or (num1 >= num3 and num2 <= num4):
                count1 += 1
            
            if (num2 >= num3 and num1 <= num4) or (num1 <= num4 and num3 <= num2):
                count2 += 1
        else:
            print("No match found")


print(f'Part 1: {count1}')
print(f'Part 2: {count2}')

        