# process command line args
import sys

# get the filename from the command line
filename = sys.argv[1]

# open the file
with open(filename) as f:
    # read the file into a list of lines
    lines = f.readlines()


 # Rock: A, X        1
# Paper: B, Y       2
# Scissors: C, Z    3

# Lose 0
# Draw 3
# Win 6

conv= {'A': 'rock', 'B': 'paper', 'C': 'scissors', 'X': 'rock', 'Y': 'paper', 'Z': 'scissors'}

score = 0
for line in lines:
      
    elf = conv[line[0]]
    player = conv[line[2]]

    if player == 'rock':
        score += 1
    elif player == 'paper':
        score += 2
    elif player == 'scissors':  
        score += 3

    if elf == player:
        score += 3
    elif elf == 'rock':
        if player == 'paper':
            score += 6
        elif player == 'scissors':
            score += 0
    elif elf == 'paper':
        if player == 'rock':
            score += 0
        elif player == 'scissors':
            score += 6
    elif elf == 'scissors':
        if player == 'rock':
            score += 6
        elif player == 'paper':
            score += 0


print(f'Part 1: {score}')

# X: Lose
# Y: Draw
# Z: Win
score = 0
for line in lines:
    elf = conv[line[0]]
    result = line[2]
    if result == 'X': # lose
        if elf == 'rock': # we play scissors
            score += 3
        elif elf == 'paper': # we play rock
            score += 1
        elif elf == 'scissors': # we play paper
            score += 2
    elif result == 'Y': # draw
        if elf == 'rock': # we play rock
            score += 4
        elif elf == 'paper': # we play paper
            score += 5
        elif elf == 'scissors': # we play scissors
            score += 6
    elif result == 'Z': # win
        if elf == 'rock': # we play paper
            score += 8
        elif elf == 'paper': # we play scissors
            score += 9
        elif elf == 'scissors': # we play rock
            score += 7

print(f'Part 2: {score}')

