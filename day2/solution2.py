puzzleinput = open("input.txt", "r")


def validate(inp):
    inp = inp.strip()
    sets = inp.split(": ")[1].split("; ")
    red, green, blue = 0, 0, 0
    for i in range(len(sets)):
        currentset = sets[i]
        values = currentset.split(", ")

        for x in range(len(values)):
            value = values[x].split(" ")
            if value[1] == "red":
                if int(value[0]) > red:
                    red = int(value[0])
            elif value[1] == "green":
                if int(value[0]) > green:
                    green = int(value[0])
            elif value[1] == "blue":
                if int(value[0]) > blue:
                    blue = int(value[0])
            print(value)
    # print(str(red) + ' * ' + str(green) + ' * ' + str(blue) + ' = ' + str(red * green * blue))
    return red * green * blue


def solve(inp):
    total = 0
    for i in range(len(inp)):
        total += validate(inp[i])
        # print(i+1)
        # print(total)

    return total


print(solve(puzzleinput.readlines()))


