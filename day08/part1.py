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

visible = set()

# From the top and bottom
for column in range(len(rows[0])):
    tallestTop = -1
    tallestBottom = -1
    for row in range(len(rows)):
        currentHeight = rows[row][column]
        if (currentHeight > tallestTop):
            visible.add((column, row))
            tallestTop = currentHeight

        # From the bottom (we can do it at the same time that we iterate columns)
        # Using this as a Y value, so only want to use positive values though negative would be more convenient
        rowBottom = len(rows) - row - 1
        currentHeight = rows[rowBottom][column]
        if (currentHeight > tallestBottom):
            visible.add((column, rowBottom))
            tallestBottom = currentHeight

# From the left and right
for rowIndex in range(len(rows)):
    row = rows[rowIndex]
    tallestLeft = -1
    tallestRight = -1
    for column in range(len(row)):
        currentHeight = row[column]
        if (currentHeight > tallestLeft):
            visible.add((column, rowIndex))
            tallestLeft = currentHeight

        # From the right (we can do it at the same time that we iterate rows)
        columnRight = len(row) - column - 1
        currentHeight = row[columnRight]
        if (currentHeight > tallestRight):
            visible.add((columnRight, rowIndex))
            tallestRight = currentHeight

for row in range(len(rows)):
    for column in range(len(rows[0])):
        if ((column, row) not in visible):
            print(' ', end='')
        else:
            print(rows[row][column], end='')
    print('\n', end='')


print(f'The number of visible trees is {len(visible)}.')
