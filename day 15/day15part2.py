f = open("input.txt", "r")

values = f.readline().replace("\n", "").split(",")
total = 0
boxes = [[] for _ in range(256)]
lenslibrary = range(1,9)

for value in values:
    label = ""
    number = 0
    mark = ""
    if "=" in value:
        label = value.split("=")[0]
        mark = "="
        number = int(value.split("=")[1])
    else:
        label = value.split("-")[0]
        mark = "-"

    curval = 0

    for character in label:
        curval += ord(character)
        curval = curval * 17
        curval = curval % 256

    i = 0

    if mark == "-":
        for lens in boxes[curval]:
            if lens[0] == label:
                del boxes[curval][i]
            i+=1
    elif mark == "=":
        found = False
        for lens in boxes[curval]:
            if lens[0] == label:
                boxes[curval][i] = (label, number)
                found = True
            i+=1
        if not found:
            boxes[curval].append((label, number))

boxnum = 0
for box in boxes:
    lensnum = 0
    for lens in box:

        focuspower = (1 + boxnum) * (lensnum + 1) * (lens[1])

        total += focuspower

        lensnum+=1
    boxnum+=1

print("TOTAL: " + str(total))