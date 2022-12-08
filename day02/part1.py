import sys

fileLocation = None
if (len(sys.argv) >= 2):
    fileLocation = sys.argv[1]
else:
    fileLocation = input(
        "Enter input file location: ")

total = 0
shapePointMap = {
    "X": 1,
    "Y": 2,
    "Z": 3
}
resultPointMap = {
    "A": {
        "X": 3,
        "Y": 6,
        "Z": 0
    },
    "B": {
        "X": 0,
        "Y": 3,
        "Z": 6
    },
    "C": {
        "X": 6,
        "Y": 0,
        "Z": 3
    }
}
with open(fileLocation) as file:
    for line in file:
        opponentMove, myMove = line.strip().split(' ')
        total += shapePointMap[myMove]
        total += resultPointMap[opponentMove][myMove]

print(f'Your score would be {total}.')
