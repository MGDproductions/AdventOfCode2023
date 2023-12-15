f = open("input.txt", "r")
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

for row in grid:
    print("".join(row))

for rowi in range(len(grid)):
    for chari in range(len(grid)):
        if grid[rowi][chari] == "O":
            load = len(grid) - rowi
            total += load

print("TOTAL: " + str(total))