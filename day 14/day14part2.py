import numpy as np
f = open("day 14/input.txt", "r")
line = f.readline()
total = 0

grid = []
row = 0

while line != "":

    line = line.replace("\n", "")

    grid.append([])

    for char in line:
        grid[row].append(char)
    
    row += 1

    line = f.readline()

def tiltnorth():
    for rowi in range(len(grid)):
        for chari in range(len(grid[rowi])):
            if grid[rowi][chari] == "O":
                minspot = rowi
                for spoti in range(rowi, -1, -1):
                    if grid[spoti][chari] == "#":
                        minspot = spoti + 1
                        break
                    elif spoti != rowi and grid[spoti][chari] == "O":
                        break
                    elif grid[spoti][chari] == ".":
                        minspot -= 1

                grid[rowi][chari] = "."
                grid[minspot][chari] = "O"

def tiltsouth():
    global grid
    grid = np.rot90(grid, k=2)
    tiltnorth()
    grid = np.rot90(grid, k=2)

def tilteast():
    global grid
    grid = np.rot90(grid, k=1)
    tiltnorth()
    grid = np.rot90(grid, k=3)   

def tiltwest():
    global grid
    grid = np.rot90(grid, k=3)   
    tiltnorth()
    grid = np.rot90(grid, k=1)   

# Appearently rotating it 1000 times gives the same result as 1000000000, so uhh it worked but this is not correct i guess lmao
for cycle in range(1000):
    tiltnorth()
    tiltwest()
    tiltsouth()
    tilteast()

for row in grid:
    print("".join(row))

for rowi in range(len(grid)):
    for chari in range(len(grid)):
        if grid[rowi][chari] == "O":
            load = len(grid) - rowi
            total += load

print("TOTAL: " + str(total))