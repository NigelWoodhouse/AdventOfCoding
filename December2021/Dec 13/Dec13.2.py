f = open("numbers.txt", "r")
lines = f.read().splitlines()
dots = [i.split(',', 1) for i in lines]

for i in range(len(dots)):
    dots[i] = [int(dots[i][0]), int(dots[i][1])]

f = open("folds.txt", "r")
coords = f.read().splitlines()
f.close()
folds = [i.split(' ', 1) for i in coords]

def grid_dimensions(fold_axis):
    x_dim = 0
    y_dim = 0
    for i in range(len(fold_axis)):
        fold_axis[i][1] = int(fold_axis[i][1])
        if fold_axis[i][0] == "x" and x_dim == 0:
            x_dim = (fold_axis[i][1] * 2) + 1
        if fold_axis[i][0] == "y" and y_dim == 0:
            y_dim = (fold_axis[i][1] * 2) + 1
    if x_dim != 0 and y_dim != 0:
        grid = [["."] * x_dim for i in range(y_dim)]
        return grid, x_dim, y_dim

def populate_grid(grid, coordinates):
    for i in range(len(coordinates)):
        grid[coordinates[i][1]][coordinates[i][0]] = "#"
    return grid

def fold(grid, fold_axis, fold_line, counter):
    y_dim = len(grid)
    x_dim = len(grid[0])

    if fold_axis == "x": # fold line is vertical
        for i in range(y_dim):
            for j in range(int((x_dim-1)/2)):
                if grid[i][x_dim-j-1] == "#":
                    grid[i][j] = "#"
            grid[i] = grid[i][:int((x_dim-1)/2)]
    
    if fold_axis == "y": # fold line is horizontal
        for i in range(int((y_dim-1)/2)):
            for j in range(x_dim):
                if grid[y_dim-i-1][j] == "#":
                    grid[i][j] = "#"
        grid = grid[:int((y_dim-1)/2)]

    for i in range(len(grid)-1):
        counter += grid[i].count(0)
    return grid, counter

grid, x_dim, y_dim = grid_dimensions(folds)
grid = populate_grid(grid, dots)
counter = 0
for line in range(len(folds)):
    grid, count = fold(grid, folds[line][0], folds[line][1], counter)
    counter += count
    print(counter)
print(grid)

with open("output.txt", 'w') as file:
    file.writelines('\t'.join(str(j) for j in i) + '\n' for i in grid)
# JRZBLGKH