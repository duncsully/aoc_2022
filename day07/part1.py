import sys


def crawlDirectory(directory, path=''):
    total = 0
    for name in directory:
        if (name != '_parent'):
            item = directory[name]
            fullName = path + '_' + name
            if (type(item) is dict):
                directoryTotal = crawlDirectory(directory[name], fullName)
                total += directoryTotal
                directorySizes[fullName] = directoryTotal
            else:
                total += int(item)
    return total


fileLocation = None
if (len(sys.argv) >= 2):
    fileLocation = sys.argv[1]
else:
    fileLocation = input(
        "Enter input file location: ")

with open(fileLocation) as file:
    root = dict()
    root['_parent'] = root
    fileSystem = {'/': root}
    activeDirectory = root
    # Build file system
    for line in file:
        parts = line.strip().split(' ')
        if (parts[0] == "$"):
            if (parts[1] == 'cd'):
                location = parts[2]
                if (location == ".."):
                    activeDirectory = activeDirectory['_parent']
                elif (location == '/'):
                    activeDirectory = fileSystem['/']
                else:
                    if (location not in activeDirectory):
                        activeDirectory[location] = {
                            '_parent': activeDirectory
                        }
                    activeDirectory = activeDirectory[location]
        # We can assume this is the results of an ls command
        else:
            name = parts[1]
            if (parts[0] == 'dir' and name not in activeDirectory):
                activeDirectory[name] = {
                    "_parent": activeDirectory
                }
            # Assume a file
            else:
                activeDirectory[name] = parts[0]

directorySizes = dict()
crawlDirectory(fileSystem)

totalSize = 0
for directoryName in directorySizes:
    size = directorySizes[directoryName]
    if (size <= 100000):
        totalSize += size

print(f'The sum of the total sizes is {totalSize}.')
