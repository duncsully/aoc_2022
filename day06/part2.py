import sys
from collections import deque

fileLocation = None
if (len(sys.argv) >= 2):
    fileLocation = sys.argv[1]
else:
    fileLocation = input(
        "Enter input file location: ")

with open(fileLocation) as file:
    lastFourteen = deque([], 14)
    line = file.readline().strip()
    for i, char in enumerate(line):
        lastFourteen.append(char)
        if (len(set(lastFourteen)) == 14):
            break
print(f'It took {i + 1} characters to start-of-packet marker')
