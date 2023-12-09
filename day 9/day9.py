import time
f = open("input.txt", "r")
line = f.readline()
total = 0

histories = []

while line != "":

    line = line.replace("\n", "")

    histories.append(list(map(int, line.split(" "))))

    line = f.readline()

for history in histories:
    tree = []
    tree.append(history)

    for row in tree:
        if (row.count(0) != len(row)):
            previousnum = 0
            differences = []
            for number in row:
                difference = int(number) - int(previousnum)
                differences.append(difference)
                previousnum = int(number)
            differences.pop(0)
            tree.append(differences)
        else:
            break
    
    tree.reverse()

    lastnumber = 0
    i = 0
    for row in tree:
        tree[i].append(row[len(row) - 1] + lastnumber)
        lastnumber = row[len(row) - 1]
        i += 1

    total += lastnumber

print("SUM: " + str(total))