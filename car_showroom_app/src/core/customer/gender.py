from enum import Enum


class Gender(Enum):
    _MALE = "Male"
    _FEMALE = "Female"

    @classmethod
    def choices(cls):
        return tuple((i.name, i.value) for i in cls)
