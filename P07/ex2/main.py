"""
Docstring for ex2.main
"""

from ex2.EliteCard import EliteCard


def main():
    """
    Main function to demonstrate the Ability System and Multiple Inheritance.
    """
    print()
    print("=== DataDeck Ability System ===")
    print()

    print("EliteCard capabilities:")
    print("Card: ['play', 'get_card_info', 'is_playable']")
    print("Combatable: ['attack', 'defend', 'get_combat_stats']")
    print("Magical: ['cast_spell', 'channel_mana', 'get_magic_stats']")

    arcane_warrior = EliteCard(
        name="Arcane Warrior",
        cost=5,
        rarity="Legendary",
        attack_power=5,
        health=10,
        mana=4
    )
    try:
        print(f"\nPlaying {arcane_warrior.name} (Elite Card):")
        print(arcane_warrior.play({"available_mana": 13}))

        print("\nCombat phase:")

        attack_result = arcane_warrior.attack("Enemy")
        print(f"Attack result: {attack_result}")

        defense_result = arcane_warrior.defend(2)
        print(f"Defense result: {defense_result}")

        print("\nMagic phase:")

        spell_result = arcane_warrior.cast_spell(
            "Fireball", ["Enemy1", "Enemy2"]
        )
        print(f"Spell cast: {spell_result}")

        channel_result = arcane_warrior.channel_mana(3)
        print(f"Mana channel: {channel_result}")

        print("\nMultiple interface implementation successful!")

    except Exception as e:
        print(e)
        print("Summon not performed")


if __name__ == "__main__":
    main()
