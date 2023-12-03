
f = open("day1.txt", "r")
line = f.readline()
sum = 0

while line != "":
    numbers = []
    characters = [*line]

    for character in characters:
        if character.isdigit():
            numbers.append(character)

    number = numbers[0] + numbers[len(numbers)- 1]

    print(number)

    sum += int(number)

    line = f.readline()

print(sum)