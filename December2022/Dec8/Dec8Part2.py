file = open("input.txt", "r")
grid = [list(line) for line in file]
for line in range(len(grid)-1):
    grid[line].pop()
row = len(grid)
column = len(grid[0])
max_scenic_score = 0
# x, y are tree position
for x in range(column):
    for y in range(row):
        # At tree, count up, down, left, right using dummy variable
        # count up
        if (x == 0 or x == column-1 or y == 0 or y == row-1):
            continue
        else:
            scenic_score = 0
            up, down, left, right = 1,1,1,1
            while ((x-up) > 0):
                if grid[x-up][y] < grid[x][y]:
                    up+=1
            while ((x+down) < column -1):
                if grid[x+down][y] < grid[x][y]:
                    down+=1
            while ((y-left) > 0):
                if grid[x][y-left] < grid[x][y]:
                    left += 1
            while ((y+right) < row -1):
                if grid[x][y+right] < grid[x][y]:
                    right+=1
            scenic_score = (up*down*left*right)
            if scenic_score > max_scenic_score:
                max_scenic_score = scenic_score
print(max_scenic_score)
# 474606
