f = open("input.txt", "r")
line = f.readline()
totals = []

races = []

racetimes = [line.replace("\n", "").split(":")[1].replace(" ", "")]
line = f.readline()
racedistances = [line.replace("\n", "").split(":")[1].replace(" ", "")]

for i in range(len(racetimes)):
    races.append([racetimes[i], racedistances[i]])

for race in races:
    raceTime = race[0]
    recordDistance = race[1]
    waystowin = 0

    for time in range(1, int(raceTime)):
        speed = int(time)

        timeLeft = int(raceTime) - time

        racedLen = speed * timeLeft

        if int(racedLen) > int(recordDistance):
            waystowin += 1
    
    if waystowin > 0:
        totals.append(waystowin)

wholetotal = 0

first = True
for total in totals:
    if first:
        wholetotal = totals[0]
        first = False
    else:
        wholetotal = wholetotal * total

print("TOTAL: " + str(wholetotal))