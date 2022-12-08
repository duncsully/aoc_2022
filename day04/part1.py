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
        if ((firstStart <= secondStart and firstEnd >= secondEnd) or (secondStart <= firstStart and secondEnd >= firstEnd)):
            fullyEnclosingPairs += 1

print(
    f'The number of pairs where one fully encloses the other is {fullyEnclosingPairs}.')
