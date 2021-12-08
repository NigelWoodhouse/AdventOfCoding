f = open("numbers.txt", "r")
lines = f.read().split("\n")

output = []

for line in lines:
    temp = line.split(' | ')[1].split(' ')
    output.append(temp)

valid_len = [2,3,4,7]
count = 0

for line in output:
    for number in line:
        if len(number) in valid_len:
            count += 1
print(count)
# 369