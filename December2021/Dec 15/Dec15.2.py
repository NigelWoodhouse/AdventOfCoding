import numpy as np
import math
with open("numbers2.txt") as f:
    file = [list(line.rstrip()) for line in f]

for i in range(len(file)):
    for j in range(len(file[0])):
        file[i][j] = int(file[i][j])

init_x = len(file[0])
init_y = len(file)

large_cave = []
for _ in range(5):
    for x in range(len(file)):
        large_cave.append(file[x].copy())
for y in range(len(large_cave)):
    large_cave[y] += large_cave[y] * 4

for ii in range(len(large_cave)):
    for jj in range(len(large_cave[0])):
        large_cave[ii][jj] += (math.floor(ii/init_x) + math.floor(jj/init_y))
        if large_cave[ii][jj] >= 10:
            large_cave[ii][jj] -= 9

with open("outfile.txt", 'w') as file:
    file.writelines(' '.join(str(j) for j in i) + '\n' for i in large_cave)

def minCost(cost, m, n):
    cost_array = [[0 for x in range(m+1)] for x in range(n+1)]
    
    cost_array[0][0] = 0
    
    for i in range(1, m+1):
        cost_array[i][0] = cost_array[i-1][0] + cost[i][0]
        
    for j in range(1, n+1):
        cost_array[0][j] = cost_array[0][j-1] + cost[0][j]
        
    for i in range(1, m+1):
        for j in range(1, n+1):
            cost_array[i][j] = min(cost_array[i-1][j], cost_array[i][j-1]) + cost[i][j]
    
    return cost_array[m][n] - cost[m][n] - min(cost[m-1][n], cost[m][n-1])

print('Minimum Cost->', minCost(large_cave, len(large_cave)-1, len(large_cave[0])-1))

# 2907