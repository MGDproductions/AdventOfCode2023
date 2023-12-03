

f = open("input.txt", "r")
line = f.readline()
sum = 0

REDCUBES = 12
GREENCUBES = 13
BLUECUBES = 14

while line != "":
    gameid = line.split(":")[0].split(" ")[1]

    games = line.split(";")

    possible = True

    for game in games:
        cubes = game.split(",")
        for cube in cubes:
            numbersAndColors = cube.replace("\n", "").split(" ")
            number = numbersAndColors[1]
            color = numbersAndColors[2]
            if "Game" in cube:
                number = numbersAndColors[2]
                color = numbersAndColors[3]
            
            if color == "red" and int(number) > REDCUBES:
                possible = False
            if color == "green" and int(number) > GREENCUBES:
                possible = False
            if color == "blue" and int(number) > BLUECUBES:
                possible = False

    if possible:
        sum += int(gameid)

    line = f.readline()

print("SUM: " + str(sum))