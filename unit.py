import random
import constraints as const
from utils import colored_text as _


class Unit:
    def __init__(self, name='Computer', health=const.HP):
        self._health = health
        self._name = name
        self._computer = True if name == 'Computer' else False
        self.steps = [
            'big_range_hit',
            'small_range_hit',
            'heal',
        ]
    
    def big_range_hit(self):
        self._health -= random.randint(*const.BIG_RANGE)

    def small_range_hit(self):
        self._health -= random.randint(*const.SMALL_RANGE)

    def heal(self):
        hp_after_heal = self._health + random.randint(*const.HEAL)
        self._health = hp_after_heal if (
            hp_after_heal <= const.HP
        ) else const.HP
    
    def step(self):
        _step = random.choice(self.steps)
        getattr(self, _step)()

        hit_color_value = self.hit_color(_step)
        print(
            f"{self}",
            f"has {self._health} HP".ljust(10, ' '), 
            _(*hit_color_value, f"<Received {_step.replace('_', ' ')}>")
        )
        self.check_heal_chance()
        return self._health
    
    def hit_color(self, _step):
        color = _step.upper() + "_COLOR"
        return getattr(const, color)
    
    def check_heal_chance(self):
        if all(
            (self._computer, 
            self.steps.count("heal") < 2,
            self._health <= const.HP * 35 / 100)
        ):
            self.steps.append("heal")
            print(_(
                *const.HEAL_INCREASED, 
                "Computer  healing chance increased!"
            ))

    def __str__(self):
        clr = const.COMPUTER_COLOR if self._computer else const.PLAYER_COLOR
        return _(*clr, self._name.ljust(8, ' '))
   