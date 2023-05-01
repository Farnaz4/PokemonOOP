from data_models.pokemon import Pokemon
from data_models.PokeType import PokeType


class grassType(Pokemon):
    def __init__(self, name, pokedexId, level, living_points, attacking_points, defence_points, attack):
        super().__init__(name, pokedexId, level, living_points, attacking_points, defence_points, attack)

        self.type: PokeType = PokeType(2)

    def lvlUp(self) -> Pokemon:
        pass
