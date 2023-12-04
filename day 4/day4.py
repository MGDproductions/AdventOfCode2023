f = open("input.txt", "r")
line = f.readline()
sum = 0

while line != "":
    line = line.replace("\n", "")

    winningnumbers = []
    scratchedwinningnumbers = []
    points = 0

    winningnumberspart = line.split(": ")[1].split("|")[0].split(" ")
    scratchednumberspart = line.split(": ")[1].split("|")[1].split(" ")

    for winningnumber in winningnumberspart:
        if winningnumber != "":
            winningnumbers.append(winningnumber)

    for scratchednumber in scratchednumberspart:
        if scratchednumber != "" and scratchednumber in winningnumbers:
            scratchedwinningnumbers.append(scratchednumber)

    i = 1
    for number in scratchedwinningnumbers:
        if i == 1:
            points = 1
        else:
            points = points * 2
        i += 1

    sum += points

    line = f.readline()

print("SUM: " + str(sum))