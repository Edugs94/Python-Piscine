"""
Docstring for ex0.main
"""

from ex0.CreatureCard import CreatureCard


def main():
    """
    Docstring for main
    """
    print("=== DataDeck Card Foundation ===")
    print()
    print("Testing Abstract Base Class Design:")

    fire_dragon: CreatureCard = CreatureCard(
        "Fire Dragon", 5, "Legendary", 7, 5
    )
    goblin_warrior = CreatureCard("Goblin Warrior", 2, "Common", 2, 3)
    print(" CreatureCard Info:")
    print(fire_dragon.get_card_info())

    print()
    print("Playing Fire Dragon with 6 mana available:")
    print("Playable:", fire_dragon.is_playable(6))
    print("Play result:", fire_dragon.play({"available_mana": 6}))

    print()
    print("Fire Dragon attacks Goblin Warrior:")
    try:
        print("Attack result:", fire_dragon.attack_target(goblin_warrior))
    except AttributeError:
        print("Target must be an object")
    except Exception:
        print("Unexpected error happened")

    print()
    print("Testing insufficient mana (3 available):")
    print("Playable:", fire_dragon.is_playable(3))

    print()
    print("Abstract pattern successfully demonstrated!")


if __name__ == "__main__":
    main()
