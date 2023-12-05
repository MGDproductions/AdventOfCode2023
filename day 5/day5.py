f = open("input.txt", "r")
line = f.readline()
lowest = None

seeds = line.replace("\n", "").split(": ")[1].split(" ")

seedToSoil = []
soilToFertilizer = []
fertilizerToWater = []
waterToLight = []
lightToTemperature = []
temperatureToHumidity = []
humidityToLocation = []

line = f.readline()
category = ""

while line != "":
    line = line.replace("\n", "")

    if ":" in line:
        category = line.split(" ")[0]
        line = f.readline()
        continue

    if len(line) > 3:
        destStart = int(line.split(" ")[0])
        sourceStart = int(line.split(" ")[1])
        rangeLength = int(line.split(" ")[2])
        if category == "seed-to-soil":
            seedToSoil.append([destStart, sourceStart, rangeLength])
        if category == "soil-to-fertilizer":
            soilToFertilizer.append([destStart, sourceStart, rangeLength])
        if category == "fertilizer-to-water":
            fertilizerToWater.append([destStart, sourceStart, rangeLength])
        if category == "water-to-light":
            waterToLight.append([destStart, sourceStart, rangeLength])
        if category == "light-to-temperature":
            lightToTemperature.append([destStart, sourceStart, rangeLength])
        if category == "temperature-to-humidity":
            temperatureToHumidity.append([destStart, sourceStart, rangeLength])
        if category == "humidity-to-location":
            humidityToLocation.append([destStart, sourceStart, rangeLength])

    line = f.readline()


for seed in seeds:
    seed = int(seed)
    foundsoil = None
    foundfertilizer = None
    foundwater = None
    foundlight = None
    foundtemperature = None
    foundhumidity = None
    foundlocation = None

    for soil in seedToSoil:
        deststart = soil[0]
        sourcestart = soil[1]
        rangeLength = soil[2]

        sourceRange = range(sourcestart, sourcestart + rangeLength)
        destRange = range(deststart, deststart + rangeLength)

        if seed in sourceRange:
            foundsoil = destRange[sourceRange.index(seed)]

    if foundsoil == None:
        foundsoil = seed

    print("----START-----")
    print(foundsoil)
    print("--------------")

    for fertilizer in soilToFertilizer:
        deststart = fertilizer[0]
        sourcestart = fertilizer[1]
        rangeLength = fertilizer[2]

        sourceRange = range(sourcestart, sourcestart + rangeLength)
        destRange = range(deststart, deststart + rangeLength)

        if foundsoil in sourceRange:
            foundfertilizer = destRange[sourceRange.index(foundsoil)]

    if foundfertilizer == None:
        foundfertilizer = foundsoil

    print(foundfertilizer)
    print("--------------")

    for water in fertilizerToWater:
        deststart = water[0]
        sourcestart = water[1]
        rangeLength = water[2]

        sourceRange = range(sourcestart, sourcestart + rangeLength)
        destRange = range(deststart, deststart + rangeLength)

        if foundfertilizer in sourceRange:
            foundwater = destRange[sourceRange.index(foundfertilizer)]

    if foundwater == None:
        foundwater = foundfertilizer

    print(foundwater)
    print("--------------")

    for light in waterToLight:
        deststart = light[0]
        sourcestart = light[1]
        rangeLength = light[2]

        sourceRange = range(sourcestart, sourcestart + rangeLength)
        destRange = range(deststart, deststart + rangeLength)

        if foundwater in sourceRange:
            foundlight = destRange[sourceRange.index(foundwater)]

    if foundlight == None:
        foundlight = foundwater

    print(foundlight)
    print("--------------")

    for temperature in lightToTemperature:
        deststart = temperature[0]
        sourcestart = temperature[1]
        rangeLength = temperature[2]

        sourceRange = range(sourcestart, sourcestart + rangeLength)
        destRange = range(deststart, deststart + rangeLength)

        if foundlight in sourceRange:
            foundtemperature = destRange[sourceRange.index(foundlight)]

    if foundtemperature == None:
        foundtemperature = foundlight

    print(foundtemperature)
    print("--------------")

    for humidity in temperatureToHumidity:
        deststart = humidity[0]
        sourcestart = humidity[1]
        rangeLength = humidity[2]

        sourceRange = range(sourcestart, sourcestart + rangeLength)
        destRange = range(deststart, deststart + rangeLength)

        if foundtemperature in sourceRange:
            foundhumidity = destRange[sourceRange.index(foundtemperature)]

    if foundhumidity == None:
        foundhumidity = foundtemperature

    print(foundhumidity)
    print("--------------")

    for location in humidityToLocation:
        deststart = location[0]
        sourcestart = location[1]
        rangeLength = location[2]

        sourceRange = range(sourcestart, sourcestart + rangeLength)
        destRange = range(deststart, deststart + rangeLength)

        if foundhumidity in sourceRange:
            foundlocation = destRange[sourceRange.index(foundhumidity)]

    if foundlocation == None:
        foundlocation = foundhumidity

    print(foundlocation)
    print("-----END------")

    if lowest == None or lowest > foundlocation:
        lowest = foundlocation

print("LOWEST: " + str(lowest))