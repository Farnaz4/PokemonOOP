from enum import Enum


class PokeType(Enum):
    Water = 0
    Fire = 1
    Grass = 2


    def __eq__(self, other):
        return True if self.name == other.name else False

    def __ne__(self, other):
        return True if self.name != other.name else False

    def __lt__(self, other):
        if self.name == other.name:
            return False

        if self.name == "Grass" and other.name == "Fire":
            return True
        if self.name == "Grass" and other.name == "Water":
            return False
        if self.name == "Water" and other.name == "Grass":
            return True
        if self.name == "Water" and other.name == "Fire":
            return False
        if self.name == "Fire" and other.name == "Grass":
            return True
        if self.name == "Fire" and other.name == "Water":
            return False

    def __gt__(self, other):
        return self.__lt__(other)
