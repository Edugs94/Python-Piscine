"""
Docstring for ft_sacred_scroll
"""

import alchemy
import alchemy.elements


def main() -> None:
    print("=== Sacred Scroll Mastery ===")
    print()
    print("Testing direct module access:")
    print("alchemy.elements.create_fire(): "
          f"{alchemy.elements.create_fire()}")
    print(
        "alchemy.elements.create_water():"
        f" {alchemy.elements.create_water()}"
    )
    print(
        "alchemy.elements.create_earth():"
        f" {alchemy.elements.create_earth()}"
    )
    print(f"alchemy.elements.create_air(): {alchemy.elements.create_air()}")

    print("\nTesting package-level access (controlled by __init__.py):")

    print(f"alchemy.create_fire(): {alchemy.create_fire()}")
    print(f"alchemy.create_water(): {alchemy.create_water()}")

    try:
        print("alchemy.create_earth():"
              f" {alchemy.create_earth()}")  # type: ignore
    except AttributeError:
        print("alchemy.create_earth(): AttributeError - not exposed")

    try:
        print(f"alchemy.create_air(): {alchemy.create_air()}")  # type: ignore
    except AttributeError:
        print("alchemy.create_air(): AttributeError - not exposed")

    print("\nPackage metadata:")
    print(f"Version: {alchemy.__version__}")
    print(f"Author: {alchemy.__author__}")


if __name__ == "__main__":
    main()
