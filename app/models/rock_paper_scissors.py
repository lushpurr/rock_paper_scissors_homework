from app.models.player import *
from app.controller import *

winner1 = Player("Ed", "Rock")
winner2 = Player("Sheila", "Scissors")
winner_list = [winner1, winner2]
hands = ["Rock", "Paper", "Scissors"]

def get_result(player1, player2):
# Rock Beats Scissors - player 1 wins
    if player1.hand == "Rock" and player2.hand == "Scissors":
        winner_list.append(player1)
        return "Rock Beats Scissors"

# Rock Beats Scissors - player 2 wins
    elif player1.hand == "Scissors" and player2.hand == "Rock":
        winner_list.append(player2)
        return "Rock Beats Scissors"
# Scissor beats paper
    elif player1.hand == "Scissors" and player2.hand == "Paper":
        winner_list.append(player1)
        return "Rock Beats Scissors"

    elif player1.hand == "Paper" and player2.hand == "Scissors":
        winner_list.append(player2)
        return "Rock Beats Scissors"

#paper beats rock
    elif player1.hand == "Paper" and player2.hand == "Rock":
        winner_list.append(player1)
        return "Paper Beats Rock"

    elif player1.hand == "Rock" and player2.hand == "Paper":
        winner_list.append(player2)
        return "Paper Beats Rock"
#draw
    elif player1.hand == player2.hand:
        return None # "It's A Draw"

# error
    else:
        return "Something's not right there. Try again."