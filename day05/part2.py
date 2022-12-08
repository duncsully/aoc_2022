import sys
from collections import deque
from itertools import repeat

fileLocation = None
if (len(sys.argv) >= 2):
    fileLocation = sys.argv[1]
else:
    fileLocation = input(
        "Enter input file location: ")

stacks = [deque([]) for i in repeat(None, 9)]
line = None
with open(fileLocation) as file:
    while (True):
        line = file.readline()
        if (line == ' 1   2   3   4   5   6   7   8   9 \n'):
            break
        # First char is at column 2, last at 35, and they exist every 4 columns
        stackIndex = 0
        for i in range(1, 35, 4):
            char = line[i]
            if (char != ' '):
                stacks[stackIndex].appendleft(char)
            stackIndex += 1

    # Empty line separating stacks from instructions
    file.readline()
    while (True):
        line = file.readline().strip()
        if (line == ''):
            break
        commandList = line.split(' ')
        amount, source, destination = map(int, commandList[1::2])
        sourceIndex = source - 1
        destinationIndex = destination - 1

        sourceStack = stacks[sourceIndex]
        if (len(sourceStack) > 0):
            maxAmount = min(amount, len(sourceStack))
            crates = deque([])
            for i in range(maxAmount):
                crates.appendleft(sourceStack.pop())
            stacks[destinationIndex].extend(crates)

topCrates = ''
for stack in stacks:
    if (len(stack) > 0):
        topCrates += stack[-1]

print(f'The code for the topmost crates is {topCrates}.')
