"""
case: A game
"""

import random


class Game:
    top_score = 0

    def __init__(self, player_name):
        self.player_name = player_name

    @staticmethod
    def show_help():
        print("game help info.")

    @classmethod
    def show_top_score(cls):
        print(f'The top score is {cls.top_score}.')

    def start_game(self):
        print(f"starting game for {self.player_name}")
        current_score = random.randint(0, 1000)
        Game.top_score = max(Game.top_score, current_score)
        print(f"{self.player_name} played game and got {current_score}")


# main
# view the game help info
Game.show_help()

# checking the current top score before playing game
Game.show_top_score()
print()

# Player Peter played game
player = "Peter"
mygame1 = Game(player)
mygame1.start_game()
Game.show_top_score()
print()

# Player Peter played game again
mygame2 = Game(player)
mygame2.start_game()
Game.show_top_score()
print()

# Player Jack played game
player = "Jack"
mygame3 = Game(player)
mygame3.start_game()
Game.show_top_score()
print()

# Player Jack played game again
mygame4 = Game(player)
mygame4.start_game()
Game.show_top_score()
