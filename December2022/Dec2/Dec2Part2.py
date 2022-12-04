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
        if game[2] == "X": # Lose
            score += (scissors + loss)
        elif game[2] == "Y": # Draw
            score += (rock + draw)
        else: # Win
            score += (paper + win)
        
    elif game[0] == "B": # Oppenent Paper
        if game[2] == "X": # Lose
            score += (rock + loss)
        elif game[2] == "Y": # Draw
            score += (paper + draw)
        else: # Win
            score += (scissors + win)

    elif game[0] == "C": # Opponent Scissors
        if game[2] == "X": # Lose
            score += (paper + loss)
        elif game[2] == "Y": # Draw
            score += (scissors + draw)
        else: # Win
            score += (rock + win)
print(score) # 11657