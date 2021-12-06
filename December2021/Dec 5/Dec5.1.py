import numpy as np
import matplotlib as plt

def load_file(file_name):
    with open(file_name,'r') as infile:
        lines = [line for line in infile]
        CO = [line.split() for line in lines]
        print(CO)
    for i in range(0, len(CO)):
        for j in range(len(CO[0])):
            CO[i][j] = int(CO[i][j])
    # print(CO)
    return CO
        # Max vale = 989, make grid 1000,1000

def load_grid(dimension):
    grid = [[0 for x in range(dimension)] for y in range(dimension)] 
    print(grid)
    return (grid)

def horizontal(grid, coordinates):
    # y is constant, go between x1, x2
    if coordinates[0] < coordinates[2]:
        # Left to Right
        for i in range(coordinates[0], coordinates[2]+1):
            grid[i][coordinates[1]] += 1
    else:
        # Right to Left
        for i in range(coordinates[2], coordinates[0]+1):
            grid[i][coordinates[1]] += 1
    return grid


def vertical(grid, coordinates):
    # x is constant, go between y1, y2
    if coordinates[1] < coordinates[3]:
        # Down to Up
        for i in range(coordinates[1], coordinates[3]+1):
            grid[coordinates[0]][i] += 1
    else:
        # Up to Down
        for i in range(coordinates[3], coordinates[1]+1):
            grid[coordinates[0]][i] += 1
    return grid

def orientation(grid, row):
    if row[0] == row[2]:
        vertical(grid, row)
    elif row[1] == row[3]:
        horizontal(grid, row)
    else:
        pass

def main():
    grid = load_grid(1001)
    CO = load_file("numbers.txt")
    for row in CO:
        orientation(grid, row)
    counter(grid)

def counter(grid):
    flatten = sum(grid, [])
    count = 0
    for i in range(len(flatten)):
        if flatten[i] > 1:
            count += 1
    print("Number of 2's or greater: ", count)
    # 6461

main()




