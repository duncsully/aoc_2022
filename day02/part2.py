import sys

fileLocation = None
if (len(sys.argv) >= 2):
    fileLocation = sys.argv[1]
else:
    fileLocation = input(
        "Enter input file location: ")

total = 0
outcomePointMap = {
    "X": 0,
    "Y": 3,
    "Z": 6
}
shapePointMap = {
    "A": {
        "X": 3,
        "Y": 1,
        "Z": 2
    },
    "B": {
        "X": 1,
        "Y": 2,
        "Z": 3
    },
    "C": {
        "X": 2,
        "Y": 3,
        "Z": 1
    }
}
with open(fileLocation) as file:
    for line in file:
        opponentMove, myMove = line.strip().split(' ')
        total += outcomePointMap[myMove]
        total += shapePointMap[opponentMove][myMove]

print(f'Your score would be {total}.')
