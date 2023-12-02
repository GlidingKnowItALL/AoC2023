import re

puzzleinput = open("input.txt", "r")


def solve(inp):
    s = 0
    for i in range(len(inp)):
        print(str(i + 1) + ': ' + return_digit(inp[i])[0] + ', ' + return_digit(inp[i])[-1] + ', ' + str(s))
        s += int(return_digit(inp[i])[0] + return_digit(inp[i])[-1])

    return s


def return_digit(inp):
    digitdict = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9"
    }
    digitbase = re.findall(r'\d|one|two|three|four|five|six|seven|eight|nine', inp)

    for i in range(len(digitbase)):
        if re.search(r'one|two|three|four|five|six|seven|eight|nine', digitbase[i]) is not None:
            digitbase[i] = digitdict[digitbase[i]]

    return digitbase

print(solve(puzzleinput.readlines()))
