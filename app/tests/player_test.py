import unittest
from models.player import Player
from models.rock_paper_scissors import *

class TestPlayer(unittest.TestCase):

    def setUp(self):
        self.player1 = Player("Player 1", "Rock")
        self.player2 = Player("Player 2", "Scissors")
        self.player3 = Player("Player 3", "Paper")

    def test_customer_has_name(self):
        self.assertEqual("Player 1", self.player1.name)

    def test_customer_has_hand(self):
        self.assertEqual("Scissors", self.player2.hand)

    def test_players_draw(self):
        result = rock_paper_scissors(self.player1, self.player1)
        self.assertEqual("It's A Draw", result)

    def test_rock_beats_scissors(self):
        result = rock_paper_scissors(self.player1, self.player2)
        self.assertEqual("Rock Beats Scissors", result)

    def test_scissors_beats_paper(self):
        result = rock_paper_scissors(self.player2, self.player3)
        self.assertEqual("Scissors Beats Paper", result)

    def test_paper_beats_rock(self):
        result = rock_paper_scissors(self.player3, self.player1)
        self.assertEqual("Paper Beats Rock", result)

