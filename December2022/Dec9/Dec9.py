import numpy as np
head_pos, tail_pos = [0,0], [0,0]
tail_pos_set = []

def calcXdist(x1, x2):
    return abs(x1-x2)
def calcYdist(y1, y2):
    return abs(y1-y2)

file = open("input.txt", "r")
for line in file:
    direction, distance = line.split(" ")
    distance = int(distance)
    for i in range(distance):
        if direction == "R":
            head_pos[0] += 1
            if calcXdist(head_pos[0], tail_pos[0]) >= 2:
                tail_pos[0] += 1
                if calcYdist(head_pos[1], tail_pos[1]) >= 1:
                    tail_pos[1] = head_pos[1]
            tail_pos_set.append(str(tail_pos[0])+':'+str(tail_pos[1]))
        elif direction == "L":
            head_pos[0] -= 1
            if calcXdist(head_pos[0], tail_pos[0]) >= 2:
                tail_pos[0] -= 1
                if calcYdist(head_pos[1], tail_pos[1]) >= 1:
                    tail_pos[1] = head_pos[1]
            tail_pos_set.append(str(tail_pos[0])+':'+str(tail_pos[1]))
        elif direction == "U":
            head_pos[1] += 1
            if calcYdist(head_pos[1], tail_pos[1]) >= 2:
                tail_pos[1] += 1
                if calcXdist(head_pos[0], tail_pos[0]) >= 1:
                    tail_pos[0] = head_pos[0]
            tail_pos_set.append(str(tail_pos[0])+':'+str(tail_pos[1]))
        elif direction == "D":
            head_pos[1] -= 1
            if calcYdist(head_pos[1], tail_pos[1]) >= 2:
                tail_pos[1] -= 1
                if calcXdist(head_pos[0], tail_pos[0]) >= 1:
                    tail_pos[0] = head_pos[0]
            tail_pos_set.append(str(tail_pos[0])+':'+str(tail_pos[1]))

unique_tail_pos_set = set(tail_pos_set)
print(len(unique_tail_pos_set)) 
# 6522