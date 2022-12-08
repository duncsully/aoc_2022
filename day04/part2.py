import sys

fileLocation = None
if (len(sys.argv) >= 2):
    fileLocation = sys.argv[1]
else:
    fileLocation = input(
        "Enter input file location: ")

fullyEnclosingPairs = 0
with open(fileLocation) as file:
    for line in file:
        first, second = line.strip().split(',')
        firstStart, firstEnd = first.split('-')
        secondStart, secondEnd = second.split('-')
        firstStart, firstEnd, secondStart, secondEnd = map(
            int, (firstStart, firstEnd, secondStart, secondEnd))
        if ((firstStart <= secondStart and firstEnd >= secondStart) or (secondStart <= firstStart and secondEnd >= firstStart)):
            fullyEnclosingPairs += 1

print(
    f'The number of pairs with any overlap is {fullyEnclosingPairs}.')
