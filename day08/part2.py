import sys

fileLocation = None
if (len(sys.argv) >= 2):
    fileLocation = sys.argv[1]
else:
    fileLocation = input(
        "Enter input file location: ")

rows = []
with open(fileLocation) as file:
    for line in file:
        rows.append(list(map(int, line.strip())))

# Brute force now, optimize later...maybe

topScenicScore = 0
position = ()
# Don't bother with the edges since the result will always be 0
for rowIndex in range(1, len(rows) - 1):
    row = rows[rowIndex]
    for columnIndex in range(1, len(row) - 1):
        cell = row[columnIndex]

        # The surrounding trees are always seen so we start our distances at 1. But don't count
        # the edge trees twice

        # Top
        topDistance = 1
        while (topIndex := rowIndex - topDistance) > 0 and (rows[topIndex][columnIndex] < cell):
            topDistance += 1

        # Bottom
        bottomDistance = 1
        while (bottomIndex := rowIndex + bottomDistance) < len(rows) - 1 and (rows[bottomIndex][columnIndex] < cell):
            bottomDistance += 1

        # Left
        leftDistance = 1
        while (leftIndex := columnIndex - leftDistance) > 0 and (row[leftIndex] < cell):
            leftDistance += 1

        # Right
        rightDistance = 1
        while (rightIndex := columnIndex + rightDistance) < len(row) - 1 and (row[rightIndex] < cell):
            rightDistance += 1

        scenicScore = topDistance * bottomDistance * leftDistance * rightDistance
        if (scenicScore > topScenicScore):
            position = (columnIndex, rowIndex)
        topScenicScore = max(scenicScore, topScenicScore)

print(f'The top scenic score is {topScenicScore} at position {position}.')
