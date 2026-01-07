import operator
from functools import reduce, partial, lru_cache, singledispatch


def spell_reducer(spells: list[int], operation: str) -> int:

    ops: dict[str, callable] = {
        "add": operator.add,
        "multiply": operator.mul,
        "max": max,
        "min": min,
    }

    if operation not in ops:
        raise ValueError(f"Unknown operation: {operation}")

    return reduce(ops[operation], spells)


def partial_enchanter(base_enchantment: callable) -> dict[str, callable]:

    return {
        "fire_enchant": partial(base_enchantment, 50, "fire"),
        "ice_enchant": partial(base_enchantment, 50, "ice"),
        "lightning_enchant": partial(base_enchantment, 50, "lightning"),
    }


@lru_cache
def memoized_fibonacci(n: int) -> int:

    if n < 0:
        raise ValueError("Position cannot be a negative value")
    if 0 <= n < 2:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> callable:
    @singledispatch
    def spell(arg) -> str:
        raise TypeError(
            "Data type must be one of the following: int, str, list"
        )

    @spell.register(int)
    def _1(arg: int) -> str:
        return f"Spell did {arg} damage"

    @spell.register(str)
    def _2(arg: str) -> str:
        return f"Spell '{arg}' selected from spellbook"

    @spell.register(list)
    def _3(arg: list) -> str:
        return f"Spell hit {arg}"

    return spell


def main():

    print("=" * 40)
    print("Testing spell reducer...")
    spells_int: list[int] = [3, 7, 2]
    try:
        print(f"Sum: {spell_reducer(spells_int, 'add')}")
        print(f"Product: {spell_reducer(spells_int, 'multiply')}")
        print(f"Max: {spell_reducer(spells_int, 'max')}")
        print(f"Min: {spell_reducer(spells_int, 'min')}")
        print(f"Not found: {spell_reducer(spells_int, 'random')}")

    except ValueError as e:
        print(e)

    print("=" * 40)
    print("Testing partial enchanter...")
    try:

        def base_enchantment(power: int, element: str, target: str) -> str:
            return (
                f"{target.capitalize()} got hit "
                f"by {element} spell of {power} power"
            )

        spell = partial_enchanter(base_enchantment)
        print(spell["fire_enchant"]("ice creature"))
        print(spell["ice_enchant"]("demon lord"))
        print(spell["lightning_enchant"]("Dragon"))
        print(spell["ground_enchanment"]("Dragon"))
    except KeyError as e:
        print(f"Enchantment {e} not existing in spellbook")

    print("=" * 40)
    print("Testing memoized fibonacci...")
    try:
        fib_position = 18
        print(f"Fib({fib_position}): {memoized_fibonacci(fib_position)}")
        stats = memoized_fibonacci.cache_info()
        print(f"Cache stats: {stats}")

        fib_position = 10000
        print(f"Fib({fib_position}): {memoized_fibonacci(fib_position)}")
        stats = memoized_fibonacci.cache_info()
        print(f"Cache stats: {stats}")
    except ValueError as e:
        print(e)
    except RecursionError:
        print("Python recursion limit reached")

    print("=" * 40)
    print("Testing spell dispatcher...")
    spell = spell_dispatcher()
    try:
        print(spell("Fireball"))
        print(spell(17))
        print(spell(["Goblin", "Dragon", "Random guy"]))
        print(spell({"example": "of_error"}))
    except TypeError as e:
        print(e)


if __name__ == "__main__":
    main()
