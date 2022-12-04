with open('input.txt') as file:
    lines = [line.rstrip() for line in file]
counter = 0

for index, line in enumerate(lines):
    if index % 3 == 0:
        common_char = list(set(lines[index]).intersection(lines[index+1]))
        common_char = list(set(common_char).intersection(lines[index+2]))[0]
        if common_char.islower():
            counter += ord(common_char)-96
        else:
            counter += ord(common_char)-38
print(counter) #2790