import numpy as np
def load(file):
    f = open(file, "r")
    lines = [list(line.rstrip()) for line in f]
    print(lines)

    #convert to int
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            lines[i][j] = int(lines[i][j])
    return(lines)

def flashes(matrix):
    count = 0

    TFM = [[False]*10 for i in range(10)]

    #Step 1 Increment 1
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            matrix[i][j] += 1

    flash_count = [0, sum(x.count(10) for x in matrix)]

    while flash_count[-2] != flash_count[-1]: # flash occured through incrementing by 1
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] >= 10 and TFM[i][j] == False:
                    TFM[i][j] = True

                    for ii in range(-1,2):
                        for jj in range(-1,2):
                            if i+ii != -1 and j+jj != -1:
                                try:
                                    if TFM[i+ii][j+jj] == False:
                                        matrix[i+ii][j+jj]+=1
                                except:
                                    pass
        temp_matrix = np.array(matrix)
        flash_count.append((temp_matrix >= 10).sum())
    
    if flash_count[-1] != 0:
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] >= 10:
                    count += 1
                    matrix[i][j] = 0

    return(matrix, count)
        

def main():
    matrix = load("numbers.txt")
    sum = 0
    counter = 0
    while sum != 100:
        sum = flashes(matrix)[1]
        counter += 1
    print(sum, counter)

main()