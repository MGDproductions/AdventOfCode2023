import math
f = open("input.txt", "r")
line = f.readline()

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

posses = []
finishes = []

for entry in map:
    if entry[0][2] == "A":
        posses.append(entry)

finish = "Z"

print(posses)

for pos in posses:
    steps = 0
    i = 0
    instruction = instructions[0]
    while True:
        steps += 1
        if i >= len(instructions):
            i = 0

        instruction = instructions[i]

        for entry in map:
            if entry[0] == pos[int(instruction)]:
                pos = entry
                break

        if pos[0][2] == finish:
            finishes.append(steps)
            break

        i += 1

def find_lcm_of_list(numbers):
    if not numbers:
        return None

    result = numbers[0]
    for num in numbers[1:]:
        result = math.lcm(result, num)

    return result

print("FINISHES: " + str(finishes))
print("LCM: " + str(find_lcm_of_list(finishes)))