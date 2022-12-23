import sys

fileLocation = None
if (len(sys.argv) >= 2):
    fileLocation = sys.argv[1]
else:
    fileLocation = input(
        "Enter input file location: ")

knots = tuple([0, 0] for _ in range(10))
visited = set([tuple(knots[-1])])
movementsMap = {
    "R": (1, 0),
    "L": (-1, 0),
    "U": (0, 1),
    "D": (0, -1)
}

with open(fileLocation) as file:
    for line in file:
        direction, number = line.strip().split(' ')
        number = int(number)
        movement = movementsMap[direction]

        for i in range(number):
            head = knots[0]
            head[0] += movement[0]
            head[1] += movement[1]
            for j in range(1, len(knots)):
                currentKnot = knots[j]
                prevKnot = knots[j - 1]

                xDif = abs(prevKnot[0] - currentKnot[0])
                yDif = abs(prevKnot[1] - currentKnot[1])

                if xDif == 2 or (xDif == 1 and yDif == 2):
                    currentKnot[0] += 1 if prevKnot[0] - \
                        currentKnot[0] > 0 else -1
                if yDif == 2 or (yDif == 1 and xDif == 2):
                    currentKnot[1] += 1 if prevKnot[1] - \
                        currentKnot[1] > 0 else -1

            visited.add(tuple(knots[-1]))

print(f'{len(visited)} positions have been visited by the tail.')
