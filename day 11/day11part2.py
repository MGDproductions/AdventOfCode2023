f = open("input.txt", "r")
line = f.readline()
sum = 0

lines = []
galaxies = []
expandingrows = []
expandingcols = []
expandingcols = []
expansioncount = 999999

# I knew i had to rectify that monstrosity of code i produced in part 1

row = 0
while line != "":

    line = line.replace("\n", "")

    lines.append(line)

    if (len(line.replace(".", "")) == 0):
        expandingrows.append(row)

    line = f.readline()
    row += 1

for i in range(len(lines[0])):
    amountofdots = 0
    for line in lines:
        if line[i] == ".":
            amountofdots+=1
    if amountofdots == len(lines):
        expandingcols.append(i)

row = 0
for line in lines:
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

            rangev = range(galaxy1[0], galaxy2[0])
            rangeh = range(galaxy1[1], galaxy2[1])

            if galaxy2[0] < galaxy1[0]:
                rangev = range(galaxy2[0], galaxy1[0])
                
            if galaxy2[1] < galaxy1[1]:
                rangeh = range(galaxy2[1], galaxy1[1])

            v = len(rangev)
            h = len(rangeh)

            for expandingrow in expandingrows:
                if expandingrow in rangev:
                    v += expansioncount

            for expandingcol in expandingcols:
                if expandingcol in rangeh:
                    h += expansioncount

            steps = v+h

            sum += steps

print("SUM: " + str(sum))
