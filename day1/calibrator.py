import re

puzzleinput = open("input.txt", "r")


def solve(inp):
    s = 0
    for i in range(len(inp)):
        s += int(re.findall(r'\d', inp[i])[0] + re.findall(r'\d', inp[i])[-1])
    return s


print(solve(puzzleinput.readlines()))
