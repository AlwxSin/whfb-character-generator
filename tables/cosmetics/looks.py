BASE_EYE = {
    'dwarf': ['Pale Grey', 'Blue', 'Copper', 'Light Brown', 'Brown', 'Dark Brown', 'Purple'],
    'elf': ['Grey Blue', 'Blue', 'Green', 'Copper', 'Light Brown', 'Brown', 'Dark Brown', 'Silver', 'Purple', 'Black'],
    'halfling': ['Blue', 'Hazel', 'Light Brown', 'Brown', 'Dark Brown'],
    'human': ['Pale Gey', 'Grey Blue', 'Blue', 'Green', 'Copper', 'Light Brown', 'Brown', 'Dark Brown', 'Purple', 'Black']
}

BASE_HAIR = {
    'dwarf': ['Ash Blond', 'Yellow', 'Red', 'Copper', 'Light Brown', 'Brown', 'Dark Brown', 'Blue Black', 'Black'],
    'elf': ['Ash Blond', 'Corn', 'Silver', 'Copper', 'Light Brown', 'Brown', 'Dark Brown', 'Yellow', 'Black'],
    'halfling': ['Ash Blond', 'Yellow', 'Red', 'Copper', 'Light Brown', 'Brown', 'Dark Brown', 'Corn', 'Black'],
    'human': ['Ash Blond', 'Yellow', 'Red', 'Copper', 'Light Brown', 'Brown', 'Dark Brown', 'Corn', 'Black']
}

BASE_WEIGHT = {
    'dwarf': [x for x in range(90, 190, 5)],
    'elf': [x for x in range(80, 180, 5)],
    'halfling': [x for x in range(75, 150, 5)],
    'human': [x for x in range(105, 225, 5)]
}

BASE_HEIGHT = {
    'M': {
        'dwarf': 4 * 12 + 4,
        'elf': 5 * 12 + 6,
        'halfling': 3 * 12 + 4,
        'human': 5 * 12 + 4
    },
    'F': {
        'dwarf': 4 * 12 + 2,
        'elf': 5 * 12 + 4,
        'halfling': 3 * 12 + 2,
        'human': 5 * 12 + 1
    }
}

BASE_AGE = {
    'dwarf': [x for x in range(20, 120, 5)],
    'elf': [x for x in range(30, 130, 5)],
    'halfling': [x for x in range(20, 62, 2)],
    'human': [x for x in range(16, 35)]
}
