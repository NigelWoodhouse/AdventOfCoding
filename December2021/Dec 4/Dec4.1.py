import numpy as np
f = open('numbers_drawn.txt', 'r')
numbers_drawn = f.readline().rstrip().split(',')
print(numbers_drawn)

f.close()
with open("bingo_cards.txt") as bingo_card:
    bingo_cards_temp = [line.split() for line in bingo_card]
    bingo_cards_temp = [x for x in bingo_cards_temp if x]
bingo_cards = bingo_cards_temp
temp_matrix = []
for i in range(len(bingo_cards_temp)):
    temp_matrix.append(bingo_cards_temp[i])
    if len(temp_matrix) % 5 == 0:
        temp_matrix = np.transpose(temp_matrix).tolist()
        for j in range(len(temp_matrix)):
            bingo_cards.append(temp_matrix[j])
        print(bingo_cards)
        temp_matrix = []

called_numbers = []
result = False
i = 0
for i in range(len(numbers_drawn)):
    if result == True:
        break
    called_numbers.append(numbers_drawn[i])
    if len(called_numbers) >= 5 and result != True:
        for j in range(len(bingo_cards)):
            result =  all(elem in called_numbers for elem in bingo_cards[j])
            # print(bingo_cards[j])
            if result == True:
                print(bingo_cards[j], called_numbers, numbers_drawn[i])
                winning_numbers = called_numbers
                print(winning_numbers)
                break

winning_board = ['19', '85', '36', '73', '71',
'65', '62', '14', '52',  '3',
'30', '83', '44', '41',  '5',
'55', '15',  '0', '61', '95',
'28', '13', '32', '31', '88']

board_sum = sum(map(int, winning_board))
for elem in winning_numbers:
    if elem in winning_board and elem in winning_numbers:
        board_sum -= int(elem)
        print(board_sum, elem)
board_sum = board_sum * int(winning_numbers[-1])
print(board_sum)

#22680