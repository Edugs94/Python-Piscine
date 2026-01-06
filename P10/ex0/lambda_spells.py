def artifact_sorter(artifacts: list[dict]) -> list[dict]:

    data: list[dict] = sorted(artifacts, key=lambda n: n["power"])
    return data


def power_filter(mages: list[dict], min_power: int) -> list[dict]:

    data: list[dict] = list(
        filter(lambda mage: mage["power"] >= min_power, mages)
    )
    return data


def spell_transformer(spells: list[str]) -> list[str]:

    data: list[str] = list(map(lambda str: "*" + str + "*", spells))
    return data


def mage_stats(mages: list[dict]) -> dict:

    powers: list[int] = list(map(lambda mage: mage["power"], mages))

    return {
        "max_power": max(powers),
        "min_power": min(powers),
        "avg_power": round(sum(powers) / len(powers), 2),
    }


def main():

    artifacts = [
        {"name": "Wind Cloak", "power": 103, "type": "accessory"},
        {"name": "Storm Crown", "power": 101, "type": "armor"},
        {"name": "Fire Staff", "power": 61, "type": "weapon"},
        {"name": "Fire Staff", "power": 87, "type": "weapon"},
    ]
    print("Testing artifact sorter...")
    print(artifact_sorter(artifacts))
    print()

    mages = [
        {"name": "Alex", "power": 98, "element": "wind"},
        {"name": "Casey", "power": 92, "element": "water"},
        {"name": "Ember", "power": 75, "element": "shadow"},
        {"name": "Riley", "power": 74, "element": "shadow"},
        {"name": "Jordan", "power": 83, "element": "shadow"},
    ]
    print("Testing power filter...")
    print(power_filter(mages, 75))
    print()

    spells = ["tsunami", "heal", "freeze", "darkness"]
    print("Testing spell transformer...")
    print(spell_transformer(spells))
    print()

    print("Testing mage stats...")
    print(mage_stats(mages))
    print()


if __name__ == "__main__":
    main()
