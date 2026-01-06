from typing import Any


def mage_counter() -> callable:
    count = 0

    def function() -> int:
        nonlocal count
        count += 1
        return count

    return function


def spell_accumulator(initial_power: int) -> callable:
    total_power = initial_power

    def function(add_power: int) -> int:
        nonlocal total_power
        total_power += add_power
        return total_power

    return function


def enchantment_factory(enchantment_type: str) -> callable:

    return lambda item: f"{enchantment_type.capitalize()} {item}"


def memory_vault() -> dict[str, callable]:

    memory: dict[str, callable] = {}

    def store(key: str, value: Any) -> None:
        memory[key] = value

    def recall(key: str) -> Any:
        return memory.get(key, "Memory not found")

    return {"store": store, "recall": recall}


def main():

    print("=" * 40)
    counter_ft = mage_counter()
    print("Testing mage counter...")
    print(counter_ft())
    print(counter_ft())
    print(counter_ft())

    print("=" * 40)
    power_ft = spell_accumulator(1000)
    print("Testing spell accumulator...")
    print(power_ft(150))
    print(power_ft(200))
    print(power_ft(250))

    print("=" * 40)
    print("Testing enchantment factory...")
    flaming = enchantment_factory("Flaming")
    frozen = enchantment_factory("Frozen")
    print(flaming("Sword"))
    print(frozen("Shield"))

    print("=" * 40)
    print("Testing memory vault...")
    my_vault = memory_vault()
    my_vault["store"]("Spell", "Fire")
    print(my_vault["recall"]("Spell"))
    print(my_vault["recall"]("Error"))


if __name__ == "__main__":
    main()
