file = open('numbers.txt', 'r')
calories = 0
elves = [0,0,0]
for line in file:
    if line.isspace():
        if calories > elves[2]:
            elves.pop()
            elves.append(calories)
            elves.sort(reverse=True)
        calories = 0
    else:
        calories += int(line)
print(sum(elves))
# 198041