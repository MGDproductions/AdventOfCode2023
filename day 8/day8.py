import time
f = open("input.txt", "r")
line = f.readline()
steps = 0

instructions = [x for x in line.replace("\n", "").replace("L", "1").replace("R", "2")]

line = f.readline()
line = f.readline()

map = []

while line != "":

    line = line.replace("\n", "")

    startpos = line.split("=")[0].replace(" ", "")
    left = line.split("(")[1].split(",")[0].replace(" ", "")
    right = line.split(",")[1].split(")")[0].replace(" ", "")

    map.append((startpos, left, right))

    line = f.readline()

for entry in map:
    if entry[0] == "AAA":
        pos = entry
        break
finish = "ZZZ"

i = 0
while True:
    steps += 1
    if i >= len(instructions):
        i = 0

    instruction = instructions[i]

    for entry in map:
        if entry[0] == pos[int(instruction)]:
            pos = entry
            break

    print(pos)

    if pos[0] == finish:
        break

    i += 1

print("STEPS: " + str(steps))