import sys

class Dir:
    def __init__(self, name: str, parent: 'Dir' = None) -> None:
        self.name = name
        self.children = {}  # dirname: Dir object
        self.files = {}  # filename: filesize
        self.parent = parent

    def __str__(self) -> str:
        return f'Dir object named {self.name} with children {self.children}'

    def addChild(self, childname: str) -> None:
        self.children[childname] = Dir(childname, self)

    def addFile(self, filename: str, filesize: int) -> None:
        self.files[filename] = filesize

    def sizeOfDir(self) -> int:
        size = sum(self.files.values())
        for child in self.children.values():
            size += child.sizeOfDir()
        return size

    def listSubDirs(self) -> None:
        for child in self.children.values():
            print(child.name)

    def listFiles(self) -> None:
        for filename, filesize in self.files.items():
            print(filename, filesize, sep='\t\t')

    def ls(self) -> None:
        self.listSubDirs()
        self.listFiles()
    
    def gotoRoot(self) -> 'Dir':
        while self.parent:
            self = self.parent
        return self


# get the filename from the command line
file = sys.argv[1]

current_level = Dir('root')
ls_state = False #
with open(file) as f:
    for line in f:
        words = line.strip().split()
        if words[0] == '$':
            ls_state = False
            if words[1] == 'cd':
                if words[2] == '/':
                    while current_level.parent:
                        current_level = current_level.parent
                elif words[2] == '..':
                    current_level = current_level.parent
                else:
                    current_level = current_level.children[words[2]]
            elif words[1] == 'ls':
                ls_state = True
            
        elif words[0] == 'dir' and ls_state:
            current_level.addChild(words[1])

        else:
            name, size = words[1], int(words[0])
            current_level.addFile(name, size)


current_level = current_level.gotoRoot()

def findSizeOfAllSubDirs(root: 'Dir') -> list[tuple[str, int]]:
    res = []
    
    # Add the size of the current directory to the result
    res.append((root.name, root.sizeOfDir()))

    # Recursively find the sizes of the subdirectories
    # recall that children is a dict with key:val -> name:object

    for child in root.children.values(): 
        res.extend(findSizeOfAllSubDirs(child))

    return res




out = findSizeOfAllSubDirs(current_level.gotoRoot())

score = 0
for dir in out:
    if dir[1] <= 100000:
        score += dir[1]

print(f'Part 1: {score}')

out.sort(key=lambda x:x[1])
sizeoffilesystem = 70000000
freespacereqd = 30000000

currentfreespace = sizeoffilesystem - out[-1][-1]


delta = freespacereqd - currentfreespace


bingo = 0
for dir in out:
    if dir[1] >= delta:
        bingo = dir[1]
        break

print(f'Part 2: {bingo}')

