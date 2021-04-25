import random

class Battle:
    def __init__(self, *players):
        self._players = players

    def execute(self):
        while True:
            player = random.choice(self._players)
            player_hp = player.step()
            if player_hp < 0:
                winner = filter(lambda p: p != player, self._players)
                print(f"{next(winner)} Win The Game!")
                break