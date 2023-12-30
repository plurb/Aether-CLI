import dataclasses


def __stat_to_mod(stat: int) -> int:
    pass


class AbilityScore:
    score: int
    modifier: int

    def __init__(self, score: int, modifier: int) -> None:
        pass

    def __str__(self):
        return f"{self.score} ({'+' if self.modifier >= 0 else ''}{self.modifier})"


class Creature:
    def __init__(self):
        self.name = ""
        self.hp = 0
        self.ac = 0
