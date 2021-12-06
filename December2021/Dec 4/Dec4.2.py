import numpy as np
from numpy.core.fromnumeric import transpose
f = open('numbers_drawn.txt', 'r')
numbers_drawn = f.readline().rstrip().split(',')
# print(numbers_drawn)
f.close()

num_lines = sum(1 for line in open('bingo_cards.txt'))+1
card_num = int(num_lines/6)
losing_count = 0
losing_board = []
for card in range(card_num):
    with open("bingo_cards.txt", 'r') as infile:
        lines = [line for line in infile][card*6:card*6+6]
        bingo_card = [line.split() for line in lines]
        bingo_card = [x for x in bingo_card if x]
        for elem in np.transpose(bingo_card).tolist():
            bingo_card.append(elem)
        print(bingo_card)

    called_numbers = []
    result = False
    count = 0
    while result == False:
        called_numbers.append(numbers_drawn[count])
        count += 1
        if count >= 5:
            for j in range(len(bingo_card)):
                result =  all(elem in called_numbers for elem in bingo_card[j])
                if result == True and count > losing_count:
                    losing_count = count
                    losing_board = bingo_card[0:5]
                    final_number = called_numbers[-1]
                    losing_numbers = called_numbers
                    called_numbers = []
                    count = 0
                    print(losing_board)
                    print(called_numbers)
                    break
                elif result == True and count < losing_count:
                    break
                else:
                    pass

print(losing_board)
print(losing_numbers)
board_sum = sum(sum([list( map(int,i) ) for i in losing_board], []))
losing_board = list(np.concatenate(losing_board).flat)            

for elem in losing_numbers:
    if elem in losing_board and elem in losing_numbers:
        board_sum -= int(elem)
        print(board_sum, elem)
board_sum = board_sum * int(final_number)
print(board_sum)    

#16168