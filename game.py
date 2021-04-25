from battle import Battle
from unit import Unit

computer = Unit()
player = Unit(name="Player")

Battle(computer, player).execute()
