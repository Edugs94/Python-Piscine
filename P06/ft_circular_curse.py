"""
Docstring for ft_circular_curse
"""

from alchemy.grimoire import record_spell, validate_ingredients


def main():
    print("=== Circular Curse Breaking ===")
    print()
    print("Testing ingredient validation:")
    print(
        f'validate_ingredients("fire air"): {validate_ingredients("fire air")}'
    )
    print(
        'validate_ingredients("dragon scales"): '
        f'{validate_ingredients("dragon scales")}'
    )

    print()
    print("Testing spell recording with validation:")
    print(
        'record_spell("Fireball", "fire air"): '
        f'{record_spell("Fireball", "fire air")}'
    )
    print(
        'record_spell("Dark Magic", "shadow"): '
        f'{record_spell("Dark Magic", "shadow")}'
    )

    print()
    print('Testing late import technique:')
    print(
        'record_spell("Lightning", "air"): '
        f'{record_spell("Lightning", "air")}'
    )

    print()
    print("Circular dependency curse avoided using late imports!")
    print("All spells processed safely!")


if __name__ == "__main__":
    main()
