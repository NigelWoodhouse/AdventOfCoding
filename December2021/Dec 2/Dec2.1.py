from os import error


f = open('numbers.txt', 'r')
content = f.readlines()

print(len(content))

h_pos = 0
v_pos = 0

for i in range(len(content)):
    move = content[i].split(' ')
    dist = int(move[1])
    if "forward" in move[0]:
        h_pos += dist
    elif "down" in move[0]:
        v_pos += dist
    elif "up" in move[0]:
        v_pos -= dist
    else:
        error()

print("Horizontal: %i Vertical: %i Product: %i" %(h_pos, v_pos, h_pos*v_pos))