from functools import cache
f = open("input.txt", "r")
line = f.readline()
sum = 0

rows = []

while line != "":

    line = line.replace("\n", "")

    rows.append(("?".join([line.split(" ")[0]] * 5), tuple(int(x) for x in line.split(" ")[1].split(","))*5))

    line = f.readline()

@cache
def calcpossibilities(springs, groups) -> int:
    if not springs:
        return len(groups) == 0

    if not groups:
        return "#" not in springs

    result = 0

    if springs[0] in ".?":
        result += calcpossibilities(springs[1:], groups)

    if (springs[0] in "#?" and groups[0] <= len(springs) and "." not in springs[:groups[0]] and (groups[0] == len(springs) or springs[groups[0]] != "#")):
        result += calcpossibilities(springs[groups[0] + 1:], groups[1:])

    return result


total = 0
for row in rows:
    total += calcpossibilities(row[0], row[1])

print(total)