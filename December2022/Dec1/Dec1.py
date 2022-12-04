file = open('numbers.txt', 'r')
calories = 0
elf = 0
for line in file:
    if line.isspace():
        if calories > elf:
            elf = calories
        calories = 0
    else:
        calories += int(line)
print(elf)
#   68787
