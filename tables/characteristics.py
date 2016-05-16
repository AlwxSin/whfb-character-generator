BASE_SECONDARY = {
    'w': 0,
    'sb': 0,
    'tb': 0,
    'mag': 0,
    'ip': 0,
    'fp': 0
}

BASE_MAIN = ['ws', 'bs', 's', 't', 'ag', 'int', 'wp', 'fel']

BASE_CHARS = {
    'dwarf': dict({
        'ws': 30,
        'bs': 20,
        's': 20,
        't': 30,
        'ag': 10,
        'int': 20,
        'wp': 20,
        'fel': 10,
        'a': 1,
        'm': 3
    }, **BASE_SECONDARY),
    'elf': dict({
        'ws': 20,
        'bs': 30,
        's': 20,
        't': 20,
        'ag': 30,
        'int': 20,
        'wp': 20,
        'fel': 20,
        'a': 1,
        'm': 5
    }, **BASE_SECONDARY),
    'halfling': dict({
        'ws': 10,
        'bs': 30,
        's': 10,
        't': 10,
        'ag': 30,
        'int': 20,
        'wp': 20,
        'fel': 30,
        'a': 1,
        'm': 4
    }, **BASE_SECONDARY),
    'human': dict({
        'ws': 20,
        'bs': 20,
        's': 20,
        't': 20,
        'ag': 20,
        'int': 20,
        'wp': 20,
        'fel': 20,
        'a': 1,
        'm': 4
    }, **BASE_SECONDARY)
}
