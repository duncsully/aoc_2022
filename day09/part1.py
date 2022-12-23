import sys

fileLocation = None
if (len(sys.argv) >= 2):
    fileLocation = sys.argv[1]
else:
    fileLocation = input(
        "Enter input file location: ")

head = [0, 0]
tail = [0, 0]
visited = set([tuple(tail)])
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
            head[0] += movement[0]
            head[1] += movement[1]

            xDif = abs(head[0] - tail[0])
            yDif = abs(head[1] - tail[1])

            if xDif == 2 or (xDif == 1 and yDif == 2):
                tail[0] += 1 if head[0] - tail[0] > 0 else -1
            if yDif == 2 or (yDif == 1 and xDif == 2):
                tail[1] += 1 if head[1] - tail[1] > 0 else -1
            visited.add(tuple(tail))

print(f'{len(visited)} positions have been visited by the tail.')
