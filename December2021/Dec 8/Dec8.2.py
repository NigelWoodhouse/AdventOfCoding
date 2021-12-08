f = open("numbers.txt", "r")
lines = f.read().split("\n")


# ------        0
# |    |    1       2
# |    |    
# ------        3
# |    |    4       5
# |    |
# ------        6

in_file = []
out_file = []
letter_list = ["a", "b", "c", "d", "e", "f", "g"]
char_5 = [3,4,5]
char_6 = [6,7,8]

def split_word(word):
    return [char for char in word]

def num_in_num(file, pair, num_length, contained_num, number): # All segments of one number in another
    for num in num_length:
        if all(item in split_word(file[num]) for item in split_word(file[contained_num])):
            pair[file[num]] = number # Add tp dictionary
            return num

def num_not_in_num(file, pair, num_length, contained_num, number):
    for num in num_length:
        if not all(item in split_word(file[num]) for item in split_word(file[contained_num])): # A segment not shared between two numbers
            pair[file[num]] = number # Add tp dictionary
            return num

def index_in_num(file, pair, num_length, index, number): # Check if contains a segment from the 7 segment display
    for num in num_length:
        if any(item in index for item in split_word(file[num])):
            pair[file[num]] = number
            return num

for line in lines: # Split line between input and output
    split = line.split(' | ')
    in_file.append(split[0].split(' '))
    out_file.append(split[1].split(' '))

# Sorting all of the numbers and characters in the numbers. All Number characters are sorted alphabetically.
# All input strings are organized in inceasing number of characters [1, 7, 4, (2,3,5), (0,6,9), 8]
for row in range(len(in_file)):
    in_file[row].sort(key=len)
    for letters in range(len(in_file[row])):
        in_file[row][letters] = "".join(sorted(in_file[row][letters]))
    for letters in range(len(out_file[row])):
        out_file[row][letters] = "".join(sorted(out_file[row][letters]))
#Store placement of known numbers
num_1 = 0
num_4 = 2
num_7 = 1
num_8 = 9
sum = 0 # Sum of output

# Need to get the order of 2,3,5,0,6,9
for element in range(len(in_file)):
    code_num_pair={}
    code_num_pair[in_file[element][num_1]] = "1" # 1
    code_num_pair[in_file[element][num_4]] = "4" # 4
    code_num_pair[in_file[element][num_7]] = "7" # 7
    code_num_pair[in_file[element][num_8]] = "8" # 8
    
    num_3 = num_in_num(in_file[element], code_num_pair, char_5, num_1,  "3") # 3
    num_9 = num_in_num(in_file[element], code_num_pair, char_6, num_3,  "9") # 9
    index_4 = list(set(letter_list)-set(split_word(in_file[element][num_9]))) # bottom left segement
    num_2 = index_in_num(in_file[element], code_num_pair, char_5, index_4,  "2") # 2
    num_5 = [x for x in char_5 if x not in [num_2, num_3]][0] 
    code_num_pair[in_file[element][num_5]] = "5" # 5
    num_0 = num_not_in_num(in_file[element], code_num_pair, char_6, num_5,  "0") # 0
    num_6 = [x for x in char_6 if x not in [num_0, num_9]][0]
    code_num_pair[in_file[element][num_6]] = "6" # 6

    holder = "" # create the number as a string
    for output in range(len(out_file[element])):
        holder += code_num_pair[out_file[element][output]] # Combine numbers in output
    sum += int(holder)
print("Sum of outputs:", sum)