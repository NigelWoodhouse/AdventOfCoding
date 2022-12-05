import re

with open('input.txt') as file:
    lines = [line.rstrip() for line in file]
# INPUT
#     [M]             [Z]     [V]    
#     [Z]     [P]     [L]     [Z] [J]
# [S] [D]     [W]     [W]     [H] [Q]
# [P] [V] [N] [D]     [P]     [C] [V]
# [H] [B] [J] [V] [B] [M]     [N] [P]
# [V] [F] [L] [Z] [C] [S] [P] [S] [G]
# [F] [J] [M] [G] [R] [R] [H] [R] [L]
# [G] [G] [G] [N] [V] [V] [T] [Q] [F]
#  1   2   3   4   5   6   7   8   9 
# HARDCODE CAUSE PARSING THIS IS DUMB
column1 = ["G", "F", "V", "H", "P", "S"]
column2 = ["G", "J", "F", "B", "V", "D", "Z", "M"]
column3 = ["G", "M", "L", "J", "N"]
column4 = ["N", "G", "Z", "V", "D", "W", "P"]
column5 = ["V", "R", "C", "B"]
column6 = ["V", "R", "S", "M", "P", "W", "L", "Z"]
column7 = ["T", "H", "P"]
column8 = ["Q", "R", "S", "N", "C", "H", "Z", "V"]
column9 = ["F", "L", "G", "P", "V", "Q", "J"]
total_columns = [[""], column1, column2, column3, column4, column5, column6, column7, column8, column9]

for line in lines:
    split_line = line.split(" ")
    num_crates = int(split_line[1])
    move_from = int(split_line[3])
    move_to = int(split_line[5])
    for elements in range(num_crates):
        total_columns[move_to].append(total_columns[move_from][(elements-num_crates)])
    for elements in range(num_crates):
        total_columns[move_from].pop()
top_crates = ''
for i in range(len(total_columns)):
    top_crates += total_columns[i][-1]
print(top_crates) # FCVRLMVQP