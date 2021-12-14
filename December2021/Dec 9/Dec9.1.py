f = open("numbers.txt", "r")
lines = [list(line.rstrip()) for line in f]

count = 0

# add 10's to top and bottom
line_length = len(lines[0])
lines.insert(0,['9']*line_length)
lines.append(['9']*line_length)

# add 10's to beginning of line and end of line
for line in range(len(lines)):
    lines[line].insert(0,'9')
    lines[line].append('9')

# convert to ints
for i in range(len(lines)):
    for j in range(len(lines[0])):
        lines[i][j] = int(lines[i][j])

# Check up, down, left, right
for i in range(len(lines)):
    for j in range(len(lines[i])):
        if lines[i][j] != 9:
            if (lines[i][j] < lines[i+1][j]) and (lines[i][j] < lines[i-1][j]) and (lines[i][j] < lines[i][j+1]) and (lines[i][j] < lines[i][j-1]):
                count += (1+ int(lines[i][j]))
                print("Success!", lines[i][j], i, j)

print("Count: ", count)
# 588