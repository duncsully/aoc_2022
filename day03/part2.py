import sys

fileLocation = None
if (len(sys.argv) >= 2):
    fileLocation = sys.argv[1]
else:
    fileLocation = input(
        "Enter input file location: ")

prioritiesTotal = 0
with open(fileLocation) as file:
    while (True):
        first = file.readline().strip()
        if (first == ''):
            break
        second = file.readline().strip()
        third = file.readline().strip()
        for char in first:
            if (char in second and char in third):
                asciiValue = ord(char)
                # Lowercase letters in range 97-122
                if (asciiValue >= 97):
                    prioritiesTotal += asciiValue - 96
                # Uppercase letters in range 65-90
                else:
                    prioritiesTotal += asciiValue - 38
                break

print(f'The total of priorities is {prioritiesTotal}.')
