import re

def number_at_index(string, target_index):
    matches = re.finditer(r'\d+', string)

    for match in matches:
        start_pos = match.start()
        end_pos = match.end()

        if start_pos <= target_index < end_pos:
            return match.group()
        
    return None

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

        numbersfound = 0
        numberrowindexes = []
        numbercolumnindexes = []
        numbers = []

        if spot == "*":

            nodiagup = False
            nodiagdown = False

            # check left
            try:
                if str(spots[rownum][spotnum - 1]).isdigit():
                    numbersfound += 1
                    numberrowindexes.append(rownum)
                    numbercolumnindexes.append(spotnum - 1)
            except:
                pass

            # check right
            try:
                if str(spots[rownum][spotnum + 1]).isdigit():
                    numbersfound += 1
                    numberrowindexes.append(rownum)
                    numbercolumnindexes.append(spotnum + 1)
            except:
                pass

            # check down
            try:
                if str(spots[rownum + 1][spotnum]).isdigit():
                    nodiagdown = True
                    numbersfound += 1
                    numberrowindexes.append(rownum + 1)
                    numbercolumnindexes.append(spotnum)
            except:
                pass

            # check up
            try:
                if str(spots[rownum - 1][spotnum]).isdigit():
                    nodiagup = True
                    numbersfound += 1
                    numberrowindexes.append(rownum - 1)
                    numbercolumnindexes.append(spotnum)
            except:
                pass

            # check diagonal
            if not nodiagdown:
                try:
                    if str(spots[rownum + 1][spotnum + 1]).isdigit():
                        numbersfound += 1
                        numberrowindexes.append(rownum + 1)
                        numbercolumnindexes.append(spotnum + 1)
                except:
                    pass

                try:
                    if str(spots[rownum + 1][spotnum - 1]).isdigit():
                        numbersfound += 1
                        numberrowindexes.append(rownum + 1)
                        numbercolumnindexes.append(spotnum - 1)
                except:
                    pass

            if not nodiagup:
                try:
                    if str(spots[rownum - 1][spotnum + 1]).isdigit():
                        numbersfound += 1
                        numberrowindexes.append(rownum - 1)
                        numbercolumnindexes.append(spotnum + 1)
                except:
                    pass

                try:
                    if str(spots[rownum - 1][spotnum - 1]).isdigit():
                        numbersfound += 1
                        numberrowindexes.append(rownum - 1)
                        numbercolumnindexes.append(spotnum - 1)
                except:
                    pass

        if numbersfound == 2:
            tuplelist = list(zip(numberrowindexes,numbercolumnindexes))

            numbers = []

            print(tuplelist)

            for tuple in tuplelist:
                numberatindex = number_at_index("".join(spots[tuple[0]]), tuple[1])
                
                if numberatindex != None:
                    numbers.append(numberatindex)

            if len(numbers) > 1 and numbers[0] != numbers[1]:
                print(numbers)
                ratio = int(numbers[0]) * int(numbers[1])
                sum += ratio

        spotnum += 1
    rownum += 1
    
print("SUM: " + str(sum))