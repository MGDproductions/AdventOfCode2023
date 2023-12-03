

f = open("input.txt", "r")
line = f.readline()
sum = 0

while line != "":
    gameid = line.split(":")[0].split(" ")[1]

    games = line.split(";")

    fewestRed = 0
    fewestGreen = 0
    fewestBlue = 0

    for game in games:

        cubes = game.split(",")

        for cube in cubes:
            numbersAndColors = cube.replace("\n", "").split(" ")
            number = numbersAndColors[1]
            color = numbersAndColors[2]
            if "Game" in cube:
                number = numbersAndColors[2]
                color = numbersAndColors[3]

            if color == "red" and int(number) > fewestRed:
                fewestRed = int(number)
            if color == "green" and int(number) > fewestGreen:
                fewestGreen = int(number)
            if color == "blue" and int(number) > fewestBlue:
                fewestBlue = int(number)

    sum += fewestRed * fewestGreen * fewestBlue

    line = f.readline()

print("SUM: " + str(sum))