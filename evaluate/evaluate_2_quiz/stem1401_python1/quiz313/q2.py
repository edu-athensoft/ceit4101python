"""
Quiz 313
q2

Two basketball teams play a game. At the end of the game,
the scoreboard shows the result of the game. If the score of
team A is higher than that of team B, the scoreboard shows
that the winner is team A. If the score of team A is lower
than that of team B, the scoreboard shows that the winner is
team B; otherwise, it shows a tie.

Please write a program for the electrical scoreboard.
Hint:	Please save your code in the file naming as
stem1401_quiz313_q2_yourname.py

"""

print("SCORE COMPARATOR")
print("Please input the two scores")

# no need to use float type but int for scores
score1 = int(input("Score for team A: "))
score2 = int(input("Score for team B: "))

result = "No result"

if score1 > score2:
    result = "Team A won!"
elif score1 < score2:
    result = "Team B won!"
else:
    result = "Tie"

print(result)

