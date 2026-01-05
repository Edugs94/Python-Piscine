"""
Docstring for ex0.lambda_spells
"""

"""
def artifact_sorter(artifacts: list[dict]) -> list[dict]
def power_filter(mages: list[dict], min_power: int) -> list[dict]
def spell_transformer(spells: list[str]) -> list[str]
def mage_stats(mages: list[dict]) -> dic
"""

def artifact_sorter(artifacts: list[dict]) -> list[dict]:

    data = sorted(artifacts, key=lambda n: n["power"])
    return data

def power_filter(mages: list[dict], min_power: int) -> list[dict]:

    data = filter(lambda mage: mage["power"] >= min_power, mages)
    return data


def main():
    artifacts = [
        {"name": "Wind Cloak", "power": 103, "type": "accessory"},
        {"name": "Storm Crown", "power": 101, "type": "armor"},
        {"name": "Fire Staff", "power": 61, "type": "weapon"},
        {"name": "Fire Staff", "power": 87, "type": "weapon"},
    ]
    print(artifact_sorter(artifacts))
    mages = [
        {'name': 'Alex', 'power': 98, 'element': 'wind'},
        {'name': 'Casey', 'power': 92, 'element': 'water'},
        {'name': 'Ember', 'power': 75, 'element': 'shadow'},
        {'name': 'Riley', 'power': 74, 'element': 'shadow'},
        {'name': 'Jordan', 'power': 83, 'element': 'shadow'}
        ]
    print(power_filter(mages, 75))



if __name__ == "__main__":
    main()


'''
=== Exercise 0 Test Data ===
# Lambda Sanctum Test Data
artifacts = [{'name': 'Fire Staff', 'power': 79, 'type': 'accessory'}, {'name': 'Wind Cloak', 'power': 99, 'type': 'weapon'}, {'name': 'Crystal Orb', 'power': 111, 'type': 'relic'}, {'name': 'Earth Shield', 'power': 103, 'type': 'armor'}]
mages = [{'name': 'Alex', 'power': 98, 'element': 'wind'}, {'name': 'Casey', 'power': 92, 'element': 'water'}, {'name': 'Ember', 'power': 75, 'element': 'shadow'}, {'name': 'Riley', 'power': 74, 'element': 'shadow'}, {'name': 'Jordan', 'power': 83, 'element': 'shadow'}]
spells = ['tsunami', 'heal', 'freeze', 'darkness']
'''