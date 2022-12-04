file = open("input.txt", "r")
score = 0
rock = 1
paper = 2
scissors = 3
loss = 0
draw = 3
win = 6
for game in file:
    game.strip()
    if game[0] == "A": # Oppenent Rock
        if game[2] == "X": # Rock
            score += (rock + draw)
        elif game[2] == "Y": # Paper
            score += (paper + win)
        else: # Scissors
            score += (scissors + loss)
        
    elif game[0] == "B": # Oppenent Paper
        if game[2] == "X": # Rock
            score += (rock + loss)
        elif game[2] == "Y": # Paper
            score += (paper + draw)
        else: # Scissors
            score += (scissors + win)

    elif game[0] == "C": # Opponent Scissors
        if game[2] == "X": # Rock
            score += (rock + win)
        elif game[2] == "Y": # Paper
            score += (paper + loss)
        else: # Scissors
            score += (scissors + draw)
print(score) # 10816