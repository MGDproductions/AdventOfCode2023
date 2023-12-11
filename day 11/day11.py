f = open("input.txt", "r")
line = f.readline()
sum = 0

lines = []
galaxies = []

while line != "":

    line = line.replace("\n", "")

    lines.append(line)

    if (len(line.replace(".", "")) == 0):
        lines.append(line)

    line = f.readline()

newlines = lines.copy()

# This is fucked up but i did this because my mind was fried after realising i didn't read correctly
expandedlines = 0
for i in range(len(lines[0])):
    amountofdots = 0
    for line in lines:
        if line[i] == ".":
            amountofdots+=1
    if amountofdots == len(lines):
        for linei in range(len(lines)):
            newlines[linei] = newlines[linei][:i + expandedlines] + '.' + newlines[linei][i + expandedlines:]
        
        expandedlines += 1

row = 0
for line in newlines:
    print(line)

    line = line.replace("\n", "")

    thing = list(line)

    col  = 0
    for char in thing:
        if char == "#":
            galaxies.append((row,col))
        col += 1

    line = f.readline()
    row += 1

for galaxy1 in galaxies:
    for galaxy2 in galaxies:
        if galaxy1 == galaxy2:
            continue

        if (galaxy2[0] > galaxy1[0]) or (galaxy1[0] == galaxy2[0] and galaxy2[1] > galaxy1[1]):
            v = galaxy2[0] - galaxy1[0]
            h = galaxy2[1] - galaxy1[1]

            steps = abs(v) + abs(h)
            print(steps)

            sum += steps

print("SUM: " + str(sum))
