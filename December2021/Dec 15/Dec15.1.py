with open("numbers.txt") as f:
    file = [list(line.rstrip()) for line in f]

for i in range(len(file)):
    for j in range(len(file[0])):
        file[i][j] = int(file[i][j])


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
    
    return cost_array[m][n] - cost[m][n]

print('Minimum Cost->', minCost(file, len(file)-1, len(file[0])-1))

#604