
f = open("day1.txt", "r")
line = f.readline()
sum = 0
writtennumbers = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}

while line != "":
    numbers = []

    characters = [*line]
    string = ""

    print(line)

    for character in characters:
        string += character
        if character.isdigit():
            numbers.append(character)
        for string2, number in writtennumbers.items():
            if str(string2) in string:
                numbers.append(str(number))
                string = "" + string[len(string)- 1]

    number = numbers[0] + numbers[len(numbers)- 1]

    print(number)

    sum += int(number)

    line = f.readline()

print(sum)