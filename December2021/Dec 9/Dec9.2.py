def matrix(file):
    f = open(file, "r")
    lines = [list(line.rstrip()) for line in f]

    lp_x = []
    lp_y = []

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
                    lp_x.append(i)
                    lp_y.append(j)
    return lines, lp_x, lp_y

def flood_fill(matrix, x, y):
    if matrix[x][y] < 9: # stop when a cell is 9
        matrix[x][y] = 10 # Set the cell to 10, and count all of the 10's later
        if x > 0:
            flood_fill(matrix,x-1,y)
        if x < len(matrix[y]) - 1:
            flood_fill(matrix,x+1,y)
        if y > 0:
            flood_fill(matrix,x,y-1)
        if y < len(matrix) - 1:
            flood_fill(matrix,x,y+1)    

def main():
    array, lp_x, lp_y = matrix("numbers.txt")
    count = [0]
    for element in range(len(lp_x)):
        flood_fill(array, lp_x[element], lp_y[element])
        count.append(sum(x.count(10) for x in array)-sum(count)) # count how many 10's there are
    count.sort(reverse=True)
    print(count[0], count[1], count[2], count[0]*count[1]*count[2])

main()
# 964712