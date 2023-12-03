
f = open("input.txt", "r")
line = f.readline()
sum = 0

spots = [[]]

i = 0
while line != "":
    line = line.replace("\n", "")
    spots.append([])

    for char in line:
        spots[i].append(char)

    i += 1

    line = f.readline()

number = ""
rownum = 0
spotnum = 0
for row in spots:
    spotnum = 0
    for spot in row:
        spot = str(spot)

        if spot.isdigit():
            number += spot
        
        if (not spot.isdigit() and number != "") or (spot.isdigit() and len(spots[rownum]) == spotnum + 1):

            numlen = len(number)
            numpos = 0
            for char in number:
                print(spotnum)
                print(numlen)
                print(numpos)
                
                numposinarr = spotnum - numlen + numpos
                numpos += 1

                print("ROW: " + str(rownum))
                print("COLUMN: " + str(numposinarr))

                # check left
                try:
                    if spots[rownum][numposinarr - 1] != "." and not str(spots[rownum][numposinarr - 1]).isdigit():
                        print("NUMBER: " + str(number))
                        sum += int(number)
                        break
                except:
                    pass

                # check right
                try:
                    if spots[rownum][numposinarr + 1] != "." and not str(spots[rownum][numposinarr + 1]).isdigit():
                        print("NUMBER: " + str(number))
                        sum += int(number)
                        break
                except:
                    pass

                # check up
                try:
                    if spots[rownum - 1][numposinarr] != "." and not str(spots[rownum - 1][numposinarr]).isdigit():
                        print("NUMBER: " + str(number))
                        sum += int(number)
                        break
                except:
                    pass

                # check down
                try:
                    if spots[rownum + 1][numposinarr] != "." and not str(spots[rownum + 1][numposinarr]).isdigit():
                        print("NUMBER: " + str(number))
                        sum += int(number)
                        break
                except:
                    pass

                # check diagonal
                try:
                    if spots[rownum + 1][numposinarr + 1] != "." and not str(spots[rownum + 1][numposinarr + 1]).isdigit():
                        print("NUMBER: " + str(number))
                        sum += int(number)
                        break
                except:
                    pass

                try:
                    if spots[rownum + 1][numposinarr - 1] != "." and not str(spots[rownum + 1][numposinarr - 1]).isdigit():
                        print("NUMBER: " + str(number))
                        sum += int(number)
                        break
                except:
                    pass

                try:
                    if spots[rownum - 1][numposinarr + 1] != "." and not str(spots[rownum - 1][numposinarr + 1]).isdigit():
                        print("NUMBER: " + str(number))
                        sum += int(number)
                        break
                except:
                    pass

                try:
                    if spots[rownum - 1][numposinarr - 1] != "." and not str(spots[rownum - 1][numposinarr - 1]).isdigit():
                        print("NUMBER: " + str(number))
                        sum += int(number)
                        break
                except:
                    pass

            number = ""
        spotnum += 1
    rownum += 1
    
print("SUM: " + str(sum))