from shapely import Point, Polygon
f = open("input.txt", "r")
line = f.readline()
steps = 0

pipes = []
start = (0,0)
i = 0

while line != "":

    line = line.replace("\n", "")

    thing = list(line)

    pipes.append(thing)

    if "S" in thing:
        start = (i, thing.index("S"))

    line = f.readline()
    i += 1


pos = start
direction = ""
loopposses = []

while True:
    if pipes[pos[0]][pos[1]] == "S" and steps > 1:
        break

    # Right
    if pipes[pos[0]][pos[1]] == "S" and pipes[pos[0]][pos[1] + 1] in ["-", "J", "7"]:
        pos = (pos[0], pos[1] + 1)
        direction = "R"
    
    # Left
    elif pipes[pos[0]][pos[1]] == "S" and pipes[pos[0]][pos[1] - 1] in ["-", "L", "F"]:
        pos = (pos[0], pos[1] - 1)
        direction = "L"

    # Up
    elif pipes[pos[0]][pos[1]] == "S" and pipes[pos[0] - 1][pos[1]] in ["|", "7", "F"]:
        pos = (pos[0] - 1, pos[1])
        direction = "U"

    # Down
    elif pipes[pos[0]][pos[1]] == "S" and pipes[pos[0] + 1][pos[1]] in ["|", "L", "J"]:
        pos = (pos[0] + 1, pos[1])
        direction = "D"

    elif pipes[pos[0]][pos[1]] == "|" and direction == "U":
        pos = (pos[0] - 1, pos[1])

    elif pipes[pos[0]][pos[1]] == "|" and direction == "D":
        pos = (pos[0] + 1, pos[1])

    elif pipes[pos[0]][pos[1]] == "-" and direction == "R":
        pos = (pos[0], pos[1] + 1)

    elif pipes[pos[0]][pos[1]] == "-" and direction == "L":
        pos = (pos[0], pos[1] - 1)

    elif pipes[pos[0]][pos[1]] == "F" and direction == "U":
        pos = (pos[0], pos[1] + 1)
        direction = "R"

    elif pipes[pos[0]][pos[1]] == "F" and direction == "L":
        pos = (pos[0] + 1, pos[1])
        direction = "D"
    
    elif pipes[pos[0]][pos[1]] == "7" and direction == "R":
        pos = (pos[0] + 1, pos[1])
        direction = "D"
    
    elif pipes[pos[0]][pos[1]] == "7" and direction == "U":
        pos = (pos[0], pos[1] - 1)
        direction = "L"

    elif pipes[pos[0]][pos[1]] == "L" and direction == "L":
        pos = (pos[0] - 1, pos[1])
        direction = "U"
    
    elif pipes[pos[0]][pos[1]] == "L" and direction == "D":
        pos = (pos[0], pos[1] + 1)
        direction = "R"

    elif pipes[pos[0]][pos[1]] == "J" and direction == "D":
        pos = (pos[0], pos[1] - 1)
        direction = "L"
    
    elif pipes[pos[0]][pos[1]] == "J" and direction == "R":
        pos = (pos[0] - 1, pos[1])
        direction = "U"

    loopposses.append(pos)
    steps += 1

steps = steps
furthest = int(steps / 2)
enlosed = 0
enclosedspots = []
a = Polygon(loopposses)

print(loopposses)

for row in range(len(pipes)):
    for col in range(len(pipes[row])):
        
        if ((row,col) not in loopposses):
            if (Point(row,col).within(a)):
                print((row,col))
                enlosed += 1
                enclosedspots.append((row,col))

print("STEPS: " + str(steps))
print("FURTHEST: " + str(furthest))
print("ENCLOSED: " + str(enlosed))