

# Which games would have been possible if the bag contained only 12 red cubes, 13 green cubes, and 14 blue cubes?

puzzleinput = open("input.txt", "r")


def validate(inp):
    game = inp.split(": ")[0].split(" ")[1]

    sets = inp.split(": ")[1].split("; ")

    for i in range(len(sets)):
        set = sets[i]

        red, green, blue = 0, 0, 0

        values = set.split(", ")
        for x in range(len(values)):
            if values[x].split(" ")[1] == "red":
                red = int(values[x].split(" ")[0])
                print("red: " + str(red))
            elif values[x].split(" ")[1] == "green":
                green = int(values[x].split(" ")[0])
                print("green: " + str(green))
            else:
                blue = int(values[x].split(" ")[0])
                print("blue: " + str(blue))

            if red > 12 or green > 13 or blue > 14:
                isvalid = False
                return int(game), isvalid

    isvalid = True
    return int(game), isvalid


def solve(inp):
    total = 0
    for i in range(len(inp)):
        if validate(inp[i])[1] is True:
            total += validate(inp[i])[0]

    return total




print(solve(puzzleinput.readlines()))


