from functools import wraps
import time
from typing import Any


def spell_timer(func: callable) -> callable:
    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        print(f"Casting {func.__name__}...")
        start = time.time()
        time.sleep(0.101)
        print(f"Spell completed in {time.time() - start:.3f} seconds")
        return func(*args, **kwargs)

    return wrapper


def power_validator(min_power: int) -> callable:
    def decorator(func: callable) -> callable:
        @wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            power_index = func.__code__.co_varnames.index("power")
            if args[power_index] >= min_power:
                return func(*args, **kwargs)
            return "Insufficient power for this spell"

        return wrapper

    return decorator


def retry_spell(max_attempts: int) -> callable:
    def decorator(func: callable) -> callable:
        @wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            for attempt in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except ValueError:
                    print(
                        "Spell failed, retrying... (attempt "
                        f"{attempt + 1}/{max_attempts})"
                    )
            return f"Spell casting failed after {max_attempts} attempts"

        return wrapper

    return decorator


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        if all(c.isalpha() or c.isspace() for c in name) and len(name) >= 3:
            return True
        return False

    def cast_spell(self, spell_name: str, power: int) -> str:
        @power_validator(10)
        def spell(power, name):
            return f"Successfully cast {name} with power {power}"

        return spell(power, spell_name)


def main():
    print("=" * 40)
    print("Testing spell timer...")

    @spell_timer
    def fireball():
        return "Fireball casted!"

    print(fireball())

    print("=" * 40)
    print("Testing power validator...")

    @power_validator(50)
    def spell(power, name):
        return f"{name} spell casted with power {power}!"

    print(spell(75, "Lightning"))
    print(spell(70, "Fireball"))
    print(spell(20, "Ice cone"))

    print("=" * 40)
    print("Testing retry spell...")

    @retry_spell(3)
    def thunder(power):
        if power > 50:
            return "Thunder casted!"
        else:
            raise ValueError

    print(thunder(10))

    print("=" * 40)
    print("Testing MagueGuild...")
    print("Testing if the following magues can join the guild:")
    print(f"Harry: {MageGuild.validate_mage_name('Harry')}")
    print(f"C-3PO: {MageGuild.validate_mage_name('C-3PO')}")
    print(f"Merlin: {MageGuild.validate_mage_name('Merlin')}")
    mage = MageGuild()
    print(f"{mage.cast_spell('Lightning', 75)}")
    print(f"{mage.cast_spell('Ember', 5)}")


if __name__ == "__main__":
    main()
