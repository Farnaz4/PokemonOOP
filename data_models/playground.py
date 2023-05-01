from data_models.pokemon import Pokemon
from data_models.waterType import waterType
from data_models.PokeType import PokeType
#squirtle = Pokemon('squirtle', '004', 10, 15, 8, 20, [('tackle', 5)])
squirtle2 = waterType('squirtle2', '004', 10, 15, 4, 6, [('tackle', 5)])
squirtle2.type.name

water = PokeType(0)
fire = Pokemon(1)

water.value == fire.value