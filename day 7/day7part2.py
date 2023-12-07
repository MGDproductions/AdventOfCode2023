from functools import cmp_to_key
f = open("input.txt", "r")
line = f.readline()
sum = 0

cards = []

while line != "":

    line = line.replace("\n", "")

    handCards = line.split(" ")[0]
    handBid = line.split(" ")[1]

    cards.append([handCards, handBid])

    line = f.readline()

possibleChars = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]

for card in cards:
    rank = 0
    maxcharcount = 0
    maxchar = ""
    oldcard = card[0]

    for char in possibleChars:
        if maxcharcount < card[0].count(char):
            maxcharcount = card[0].count(char)
            maxchar = char

    if maxchar == "J" and len(card[0].replace("J", "")) > 0:
        card[0] = card[0].replace("J", card[0].replace("J", "")[0])
    else: 
        card[0] = card[0].replace("J", maxchar)

    for char in possibleChars:
        if maxcharcount < card[0].count(char):
            maxcharcount = card[0].count(char)
            maxchar = char

    if maxcharcount == 5:
        rank = len(cards)
        #print("Five of a kind")
    elif maxcharcount == 4:
        rank = len(cards) - 1
        #print("Four of a kind")
    elif maxcharcount == 3:
        for char1 in possibleChars:
            if char1 != maxchar and card[0].count(char1) == 2:
                rank = len(cards) - 2
                #print("Full house")
                break
            
        if rank == 0:
            rank = len(cards) - 3
            #print("Three of a kind")
    elif maxcharcount == 2:
        for char1 in possibleChars:
            if char1 != maxchar and card[0].count(char1) == 2:
                rank = len(cards) - 4
                #print("Two pair")
                break
            
        if rank == 0:
            rank = len(cards) - 5
            #print("One pair")
    
    if rank == 0:
        #print("High cards")
        rank = len(cards) - 6

    card[0] = oldcard
    card.append(str(rank))

def compareByRank(item1, item2):
    if int(item1[2]) < int(item2[2]):
        return -1
    elif int(item1[2]) > int(item2[2]):
        return 1
    else:
        return 0

def compareByCard(cards1, cards2):
    for char1, char2 in zip(cards1[0], cards2[0]):
        if possibleChars.index(char1) < possibleChars.index(char2):
            return 1
        elif possibleChars.index(char1) > possibleChars.index(char2):
            return -1
    return 0

cards = sorted(cards, key=cmp_to_key(compareByCard))
cards = sorted(cards, key=cmp_to_key(compareByRank))

index = 0
for card in cards:
    index += 1
    sum += int(card[1]) * index

print(sum)