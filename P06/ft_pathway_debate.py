"""
Docstring for ft_pathway_debate
"""

from alchemy.transmutation import basic
from alchemy.transmutation import advanced
import alchemy.transmutation


def main() -> None:
    print("=== Pathway Debate Mastery ===")

    print()
    print("Testing Absolute Imports (from basic.py):")
    print(f"lead_to_gold(): {basic.lead_to_gold()}")
    print(f"stone_to_gem(): {basic.stone_to_gem()}")

    print()
    print("Testing Relative Imports (from advanced.py):")
    print(f"philosophers_stone(): {advanced.philosophers_stone()}")
    print(f"elixir_of_life(): {advanced.elixir_of_life()}")

    print()
    print("Testing Package Access:")
    print(
        "alchemy.transmutation.lead_to_gold():"
        f" {alchemy.transmutation.lead_to_gold()}"
    )
    print(
        "alchemy.transmutation.philosophers_stone():"
        f" {alchemy.transmutation.elixir_of_life()}"
    )

    print()
    print("Both pathways work! Absolute: clear, Relative: concise")


if __name__ == "__main__":
    main()
