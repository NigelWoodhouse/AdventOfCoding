import numpy as np
knot_positions = {"head": [0,0], "first": [0,0], "second": [0,0], "third": [0,0], "fourth": [0,0], "fifth": [0,0], "sixth": [0,0], "seventh": [0,0], "eighth": [0,0], "tail": [0,0]}
tail_pos_set = []

def calcXdist(x1, x2):
    return abs(x1-x2)
def calcYdist(y1, y2):
    return abs(y1-y2)
def movement_head(head_pos, direction):
    if direction == "R":
        head_pos[0] += 1
    elif direction == "L":
        head_pos[0] -= 1
    elif direction == "U":
        head_pos[1] += 1
    elif direction == "D":
        head_pos[1] -= 1

def movement(head_pos, tail_pos, save):
    if calcXdist(head_pos[0], tail_pos[0]) >= 2 and calcYdist(head_pos[1], tail_pos[1]) >=2:
        tail_pos[0] += int((head_pos[0] - tail_pos[0])/2)
        tail_pos[1] += int((head_pos[1] - tail_pos[1])/2)
    elif calcXdist(head_pos[0], tail_pos[0]) >= 2:
        tail_pos[0] += int((head_pos[0] - tail_pos[0])/2)
        tail_pos[1] = head_pos[1]
    elif calcYdist(head_pos[1], tail_pos[1]) >= 2:
        tail_pos[1] += int((head_pos[1] - tail_pos[1])/2)
        tail_pos[0] = head_pos[0]
    if save == "tail":
        tail_pos_set.append(str(tail_pos[0])+':'+str(tail_pos[1]))

file = open("input.txt", "r")
for line in file:
    direction, distance = line.split(" ")
    distance = int(distance)
    keys = list(knot_positions.keys())
    for j in range(distance):        
        for i in range(len(keys)-1):
            if i == 0:
                movement_head(knot_positions[keys[i]], direction)
            movement(knot_positions[keys[i]], knot_positions[keys[i+1]], keys[i+1])

unique_tail_pos_set = set(tail_pos_set)
print(unique_tail_pos_set)
print(len(unique_tail_pos_set)) 
# 2717