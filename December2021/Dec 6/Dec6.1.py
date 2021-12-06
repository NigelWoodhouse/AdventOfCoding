f = open("numbers.txt", "r")
fish = f.readline().split(",")
fish = list(map(int, fish))

for day in range(1,81):
    print(day)
    for element in range(len(fish)):
        if fish[element] == 0:
            fish[element] = 6
            fish.append(8)
        else:
            fish[element] -= 1
print(len(fish))
# 379414
