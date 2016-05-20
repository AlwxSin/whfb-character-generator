from random import randint, choice
from tables import careers, characteristics, fate_points, talents, wounds, skills
from tables.cosmetics import looks, names, others


class CharacterGenerator:

    races_list = ['human', 'elf', 'halfling', 'dwarf']
    sex_list = ['F', 'M']

    characteristics = {}
    cosmetics = {}
    skills =[]
    talents = []
    career = None

    def __init__(self, race, sex):
        if race in self.races_list and sex in self.sex_list:
            self.race = race
            self.sex = sex

            self.characteristics = characteristics.BASE_CHARS[self.race]

            self.calc_main()
            self.calc_secondary()

            self.get_skills()
            self.get_talents()
            self.get_career()

            self.get_cosmetics()
        else:
            raise Exception

    def d10rand(self):
        return randint(1, 10)

    def d100rand(self):
        return randint(1, 100)

    def calc_main(self):
        for char in characteristics.BASE_MAIN:
            self.characteristics[char] += (self.d10rand() + self.d10rand())

    def calc_secondary(self):
        race_wounds = wounds.STARTING_WOUNDS[self.race]
        race_fate_points = fate_points.STARTING_FATE_POINTS[self.race]
        s = self.characteristics['s']
        t = self.characteristics['t']
        self.characteristics['w'] = randint(race_wounds['min'], race_wounds['max'])
        self.characteristics['sb'] = int(str(s)[0])
        self.characteristics['tb'] = int(str(t)[0])
        self.characteristics['fp'] = randint(race_fate_points['min'], race_fate_points['max'])

    def get_cosmetics(self):
        self.cosmetics['eyes'] = choice(looks.BASE_EYE[self.race])
        self.cosmetics['hair'] = choice(looks.BASE_HAIR[self.race])
        self.cosmetics['age'] = choice(looks.BASE_AGE[self.race])

        heigth = looks.BASE_HEIGHT[self.sex][self.race] + self.d10rand()
        feets = int(heigth / 12)
        inches = heigth - feets * 12
        cm = int(round(heigth * 2.54))
        self.cosmetics['heigth'] = "{}'{} feets / {} cm".format(feets, inches, cm)

        weigth = choice(looks.BASE_WEIGHT[self.race])
        kg = int(round(weigth / 2.2046))
        self.cosmetics['weigth'] = "{} pounds / {} kgs".format(weigth, kg)

        self.cosmetics['marks'] = choice(others.BASE_MARKS)
        self.cosmetics['sign'] = choice(others.BASE_SIGN)
        self.cosmetics['siblings'] = choice(others.BASE_SIBLINGS[self.race])

        self.cosmetics['name'] = choice(names.BASE_NAMES[self.sex][self.race])

    def get_skills(self):
        self.skills = skills.BASE_SKILLS[self.race]

    def get_talents(self):
        self.talents = talents.RACE_TALENTS[self.race]
        for talent in self.talents:
            self.apply_talent(talent)

    def apply_talent(self, talent):
        chars = talent['chars'] if 'chars' in talent else []
        for char in chars:
            self.characteristics[char] += chars[char]

    def get_career(self):
        pass
