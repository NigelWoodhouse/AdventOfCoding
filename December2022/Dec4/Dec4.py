with open('input.txt') as file:
    lines = [line.rstrip() for line in file]

contain_counter = 0
for line in lines:
    x, y = line.split(',')
    x1, x2 = x.split('-') #4-5, 47-47, 4-71
    y1, y2 = y.split('-') #5-15, 47-48, 36-72
    x1 = int(x1)
    x2 = int(x2)
    y1 = int(y1)
    y2 = int(y2)

    if (y1 <= x1 and y2 >= x2) or (x1 <= y1 and x2 >= y2): # contains or endpoints are equal

        if (x1==x2==y1==y2): # all the same
            contain_counter += 1
        elif (x2 == y1 and x1 > y2): # 47-47, 47-48
            continue
        elif (x1 == y2 and x2 < y1):
            continue
        else:
            contain_counter += 1
print(contain_counter) #485