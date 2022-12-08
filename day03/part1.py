import sys

fileLocation = None
if (len(sys.argv) >= 2):
    fileLocation = sys.argv[1]
else:
    fileLocation = input(
        "Enter input file location: ")

prioritiesTotal = 0
with open(fileLocation) as file:
    for line in file:
        midPoint = len(line) // 2
        firstCompartment = line[:midPoint]
        secondCompartment = line[midPoint:]
        for char in firstCompartment:
            if (char in secondCompartment):
                asciiValue = ord(char)
                # Lowercase letters in range 97-122
                if (asciiValue >= 97):
                    prioritiesTotal += asciiValue - 96
                # Uppercase letters in range 65-90
                else:
                    prioritiesTotal += asciiValue - 38
                break

print(f'The total of priorities is {prioritiesTotal}.')
