import pprint
from generator import CharacterGenerator

char = CharacterGenerator('human', 'M')

pp = pprint.PrettyPrinter(indent=4)
pp.pprint(char.characteristics)
pp.pprint(char.cosmetics)
pp.pprint(char.career)
