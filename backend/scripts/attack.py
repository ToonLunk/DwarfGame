# stats of types of units
unit_stats = {
    "scouts": {
        "attack": 10,
        "defence": 2,
        "cost": 5
    },
    "soldiers": {
        "attack": 20,
        "defence": 10,
        "cost": 10
    },
    "mechs": {
        "attack": 50,
        "defence": 25,
        "cost": 50
    },
    "super mechs": {
        "attack": 100,
        "defence": 50,
        "cost": 100
    }
}

# stats of types of bases; level will be used to calculate the defence power. 
base_stats = {
    "inner-base": {
        "defence": 100,
        "cost": 100
    },
    "outer-base": {
        "defence": 50,
        "cost": 50
    }
}

# test data for test attack

attacker = {
    "name": "Toon Lunk",
    "attack-location": "inner-base",
    "attack-units": {
        "scouts": 300,
        "soldiers": 150,
        "mechs": 20,
        "super mechs": 5
    }  
}

defender = {
    "name": "Defender 1",
    "inner-base-units": {
        "scouts": 0,
        "soldiers": 100,
        "mechs": 100,
        "super mechs": 20
    },
    "outer-base-units": {
        "scouts": 0,
        "soldiers": 500,
        "mechs": 20,
        "super mechs": 1
    },
    "mining-fields-units": {
        "scouts": 250,
        "soldiers": 50,
        "mechs": 0,
        "super mechs": 0
    },
    "inner-base-level": 5,
    "outer-base-level": 3,
}

def attack(attacker, defender):
    # nothing yet
    pass
