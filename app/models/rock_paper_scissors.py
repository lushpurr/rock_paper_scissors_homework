from app.models.player import *


def rock_paper_scissors(player1, player2):
# Rock Beats Scissors
    if player1.hand == "Rock" and player2.hand == "Scissors":
        return "Rock Beats Scissors"
# Scissor beats paper
    elif player1.hand == "Scissors" and player2.hand == "Paper":
        return "Scissors Beats Paper"

#paper beats rock
    elif player1.hand == "Paper" and player2.hand == "Rock":
        return "Paper Beats Rock"
#draw
    elif player1.hand == player2.hand:
        return "It's A Draw"