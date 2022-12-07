import sys

fileLocation = None
if (len(sys.argv) >= 2):
    fileLocation = sys.argv[1]
else:
    fileLocation = input(
        "Enter input file location: ")

with open(fileLocation) as file:
    maxCalories = 0
    total = 0
    last = 0
    for line in file:
        if (line != "\n"):
            total += int(line)
        else:
            maxCalories = max(total, maxCalories)
            last = total
            total = 0
# Technically need to check the last line.
maxCalories = max(last, maxCalories)

print(
    f"The maximum number of calories is {maxCalories}.")
