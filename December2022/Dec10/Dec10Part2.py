import numpy as np
import math
cycleNum = 0
varX = 1
pixelArray = ["."]*240

def incrementSignalStrength(cycleNum, varX):
    cycleNum += 1
    screenLine = math.floor(cycleNum/40)
    print(cycleNum, varX, varX+3)
    if cycleNum in range(varX+(screenLine*40), varX+(screenLine*40)+3):
        pixelArray[cycleNum-1] = "#"
    return cycleNum

file = open("input.txt", "r")
for line in file:
    command = line.split(' ')
    if command[0] == "noop\n" or command[0] == "noop":
        cycleNum= incrementSignalStrength(cycleNum, varX)
    else:
        cycleNum= incrementSignalStrength(cycleNum, varX)
        cycleNum= incrementSignalStrength(cycleNum, varX)
        varX += int(command[1])
pixelArray = np.reshape(pixelArray, (6,40))
for line in pixelArray:
    with open("output.txt", "a") as f:
        for char in line:
            f.write(char)
        f.write("\n")
###..#..#.###....##.###..###..#.....##.#
#..#.#.#..#..#....#.#..#.#..#.#....#..#.
#..#.##...#..#....#.###..#..#.#....#..#.
###..#.#..###.....#.#..#.###..#....####.
#.#..#.#..#....#..#.#..#.#....#....#..#.
#..#.#..#.#.....##..###..#....####.#..#.
        
# RKPJBPLA