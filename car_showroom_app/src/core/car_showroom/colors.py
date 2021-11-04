from enum import Enum


class Color(Enum):
    _RED = "Red"
    _ORANGE = "Orange"
    _YELLOW = "Yellow"
    _GREEN = "Green"
    _BLUE = "Blue"
    _PURPLE = "Purple"
    _PINK = "Pink"
    _BLACK = "Black"
    _WHITE = "White"
    _GRAY = "Gray"

    @classmethod
    def choices(cls):
        return tuple((i.name, i.value) for i in cls)
