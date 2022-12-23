import sys

fileLocation = None
if (len(sys.argv) >= 2):
    fileLocation = sys.argv[1]
else:
    fileLocation = input(
        "Enter input file location: ")

registerX = 1
bufferedRegisterXChange = 0
cycle = 0
awaitingCycles = 0
line = None
pixels = []
with open(fileLocation) as file:
    while (True):
        # Draw pixel
        column = cycle % 40
        pixels.append('#' if abs(registerX - column) <= 1 else '.')
        if (cycle and column == 39):
            pixels.append('\n')
        # No current instruction, read new one
        if not awaitingCycles:
            line = file.readline()
            if not line:
                break
            instruction = line.strip().split(' ')

            if instruction[0] == 'addx':
                awaitingCycles = 1
                bufferedRegisterXChange = int(instruction[1])
        # Instruction active, wait
        else:
            awaitingCycles -= 1
            # Finish add instruction
            if not awaitingCycles and bufferedRegisterXChange:
                registerX += bufferedRegisterXChange
                bufferedRegisterXChange = 0
        cycle += 1

print(''.join(pixels))
