import sys

fileLocation = None
if (len(sys.argv) >= 2):
    fileLocation = sys.argv[1]
else:
    fileLocation = input(
        "Enter input file location: ")

with open(fileLocation) as file:
    first = 0
    second = 0
    third = 0
    total = 0
    last = 0
    for line in file:
        if (line != "\n"):
            total += int(line)
        else:
            if (total >= first):
                first, second, third = total, first, second
            elif (total >= second):
                second, third = total, second
            elif (total > third):
                third = total
            last = total
            total = 0
# Technically need to check the last line.
if (total >= first):
    first, second, third = total, first, second
elif (total >= second):
    second, third = total, second
elif (total > third):
    third = total

print(
    f"The total calories of the top 3 is {first + second + third}.")
