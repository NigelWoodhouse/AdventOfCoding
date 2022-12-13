file = open("input.txt", "r")
grid = [list(line) for line in file]
for line in range(len(grid)-1):
    grid[line].pop()
row = len(grid)
column = len(grid[0])
tree_count = 0
# x, y are tree position
for x in range(column):
    for y in range(row):
        # At tree, count up, down, left, right using dummy variable
        # count up
        if (x == 0 or x == column-1 or y == 0 or y == row-1):
            tree_count += 1
        else:
            visible = [True, True, True, True]
            up, down, left, right = 1,1,1,1
            while ((x-up) >= 0):
                if grid[x-up][y] < grid[x][y]:
                    up+=1
                else:  
                    visible[0] = False
                    break
            while ((x+down) < column):
                if grid[x+down][y] < grid[x][y]:
                    down+=1
                else: 
                    visible[1] = False
                    break
            while ((y-left) >= 0):
                if grid[x][y-left] < grid[x][y]:
                    left += 1
                else: 
                    visible[2] = False
                    break
            while ((y+right) < row):
                if grid[x][y+right] < grid[x][y]:
                    right+=1
                else: 
                    visible[3] = False
                    break
            if any(visible) == True:    
                tree_count += 1
print(tree_count)
# 1782