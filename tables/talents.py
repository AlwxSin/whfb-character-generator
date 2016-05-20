from random import choice

RANDOM_TALENTS = {
    'Acute Hearing': {'text': "+20% to perception checks when listening"},
    'Ambidextrous': {'text': "Do not suffer -20% WS or BS penalty when using a weapon in secondary hand"},
    'Coolheaded': {'chars': {'wp': 5}},
    'Excellent Vision': {'text': "+10% to perception checks when seeing or leap reading"},
    'Fleet Footed': {'chars': {'m': 1}},
    'Hardy': {'chars': {'w': 1}},
    'Lightning Reflexes': {'chars': {'ag': 5}},
    'Luck': {'text': "Gain extra FP each day"},
    'Marksman': {'chars': {'bs': 5}},
    'Mimic': {'text': "You can mimic. See description."},
    'Night Vision': {'text': "Can see for 30 yards. Like low-lite vision."},
    'Resistance to Disease': {'text': "+10% WP"},
    'Resistance to Magic': {'text': "+10% WP"},
    'Resistance to Poison': {'text': "+10% WP"},
    'Savvy': {'chars': {'int': 5}},
    'Sixth Sense': {'text': "GM can tell you things, when comething happens."},
    'Strong-minded': {'text': "Strong against insanity. See description."},
    'Sturdy': {'text': "No penalty in heavy armour"},
    'Suave': {'chars': {'fel': 5}},
    'Super Numerate': {'text': "You can calc. See description."},
    'Very Resilent': {'chars': {'t': 5}},
    'Very Strong': {'chars': {'s': 5}},
    'Warrior Born': {'chars': {'ws': 5}}
}

OTHER_TALENTS = {
    'Dwarfcraft': {'text': "+10% Trade skills. See description."},
    'Grudge-born Fury': {'text': "+5% WS against orcs, (hob)goblins"},
    'Stout-hearted': {'text': "+10% against fear and terror test or WP against intimidate"},
    'Aethyric Attunement': {'text': "+10% to Channeling & Magical Sense Skill Tests"},
    'Specialist Weapon Group (Longbow)': {},
    'Specialist Weapon Group (Sling)': {},
    'Resistance to Chaos': {'text': "+10% WP"},
}

def get_talents_halfling():
    talents = [
        RANDOM_TALENTS['Night Vision'],
        OTHER_TALENTS['Resistance to Chaos'],
        OTHER_TALENTS['Specialist Weapon Group (Sling)']
    ]
    random_talent = RANDOM_TALENTS[choice(RANDOM_TALENTS.keys())]
    while random_talent in talents:
        random_talent = RANDOM_TALENTS[choice(RANDOM_TALENTS.keys())]
    talents.append(random_talent)

    return talents

def get_talents_human():
    talents = []
    keys = set()
    while len(keys) < 2:
        keys.add(choice(RANDOM_TALENTS.keys()))
    for key in keys:
        talents.append(RANDOM_TALENTS[key])
    return talents

RACE_TALENTS = {
    'dwarf': [
        OTHER_TALENTS['Dwarfcraft'], OTHER_TALENTS['Grudge-born Fury'],
        RANDOM_TALENTS['Night Vision'], RANDOM_TALENTS['Resistance to Magic'],
        OTHER_TALENTS['Stout-hearted'], RANDOM_TALENTS['Sturdy']
    ],
    'elf': [
        [
            OTHER_TALENTS['Aethyric Attunement'],
            OTHER_TALENTS['Specialist Weapon Group (Longbow)']
        ],
        [
            RANDOM_TALENTS['Coolheaded'],
            RANDOM_TALENTS['Savvy']
        ],
        RANDOM_TALENTS['Excellent Vision'], RANDOM_TALENTS['Night Vision']
    ],
    'halfling': get_talents_halfling(),
    'human': get_talents_human()
}
