f = open("input.txt", "r")
line = f.readline()
sum = 0

cards = []

while line != "":
    line = line.replace("\n", "")

    cards.append(line)

    line = f.readline()

cardindex = 0
originalcards = cards
for card in cards:
    cardnumber = int(card.split(":")[0].replace("Card", "").replace(" ", ""))
    winningnumbers = []

    winningnumberspart = card.split(": ")[1].split("|")[0].split(" ")
    scratchednumberspart = card.split(": ")[1].split("|")[1].split(" ")

    for winningnumber in winningnumberspart:
        if winningnumber != "":
            winningnumbers.append(winningnumber)

    i = cardnumber
    for scratchednumber in scratchednumberspart:
        if scratchednumber != "" and scratchednumber in winningnumbers:
            if i < len(originalcards):
                cards.append(originalcards[i])
                i += 1

print("SUM: " + str(len(cards)))