f = open("input.txt", "r")

values = f.readline().replace("\n", "").split(",")
total = 0

for value in values:
    curval = 0
    for character in value:
        curval += ord(character)
        curval = curval * 17
        curval = curval % 256

    total += curval

print("TOTAL: " + str(total))