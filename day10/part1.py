import sys

fileLocation = None
if (len(sys.argv) >= 2):
    fileLocation = sys.argv[1]
else:
    fileLocation = input(
        "Enter input file location: ")

registerX = 1
bufferedRegisterXChange = 0
cycle = 1
awaitingCycles = 0
line = None
signalStrengthSum = 0
with open(fileLocation) as file:
    while (True):
        # Check if on a signal strength cycle
        if ((cycle - 20) % 40 == 0):
            signalStrengthSum += cycle * registerX
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

print(f'The sum of the signal strengths is {signalStrengthSum}.')
