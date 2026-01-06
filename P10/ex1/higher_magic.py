def spell_combiner(spell1: callable, spell2: callable) -> callable:
    return lambda *args, **kwargs: (
        spell1(*args, **kwargs),
        spell2(*args, **kwargs),
    )


def power_amplifier(base_spell: callable, multiplier: int) -> callable:
    return lambda *args, **kwargs: base_spell(*args, **kwargs) * multiplier


def conditional_caster(condition: callable, spell: callable) -> callable:
    return lambda *args, **kwargs: (
        spell(*args, **kwargs)
        if condition(*args, **kwargs)
        else "Spell fizzled"
    )


def spell_sequence(spells: list[callable]) -> callable:
    return lambda *args, **kwargs: [s(*args, **kwargs) for s in spells]


def main():
    print("=" * 40)
    print("Testing spell combiner...")

    def fireball(creature) -> str:
        return f"Fireball hits {creature}"

    def heal(creature) -> str:
        return f"Heals {creature}"

    def freeze(creature) -> str:
        return f"{creature} has been frozen"

    combined = spell_combiner(fireball, heal)
    result_tuple = combined("Dragon")
    result_text = ", ".join(result_tuple)
    print(f"Combined spell result: {result_text}")
    print("=" * 40)
    print("Testing power amplifier...")

    def base_spell() -> int:
        return 10

    amp_power = power_amplifier(base_spell, 3)
    print(f"Original: {base_spell()}, Amplified: {amp_power()}")

    print("=" * 40)
    print("Testing conditional caster...")

    def condition(creature) -> bool:
        if creature is None:
            return False
        return True

    castif = conditional_caster(condition, freeze)
    print(f"Casting spell: {castif('Goblin')}")

    print("=" * 40)
    print("Testing spell sequence...")
    concatenated_spells = spell_sequence([fireball, heal, freeze])
    print(f"Casting spells in order: {concatenated_spells('Goblin')}")


if __name__ == "__main__":
    main()
