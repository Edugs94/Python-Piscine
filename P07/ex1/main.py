"""
Docstring for ex1.main
"""

from typing import List, Optional
from ex0.Card import Card
from ex0.CreatureCard import CreatureCard as Creature
from ex1.SpellCard import SpellCard as Spell, UnknownEffect
from ex1.ArtifactCard import ArtifactCard as Artifact
from ex1.Deck import Deck


def main() -> None:
    """
    Main execution function for DataDeck demonstration.
    """
    print("=== DataDeck Deck Builder ===")
    print()

    print("Building deck with different card types...")
    cards_list: List[Card] = []

    try:
        fire_dragon: Creature = Creature("Fire Dragon", 5, "Legendary", 7, 5)
        mana_crystal: Artifact = Artifact(
            "Mana Crystal", 3, "Common", 3, "Permanent: +1 mana per turn"
        )
        lighting_bolt: Spell = Spell("Lightning Bolt", 4, "Rare", "damage")

        cards_list.extend([fire_dragon, mana_crystal, lighting_bolt])

    except UnknownEffect as e:
        print(f"[SUCCESS] Caught expected validation error: {e}")
    except ValueError as e:
        print(f"[ERROR] Value error caught: {e}")
    except Exception as e:
        print(f"[ERROR] Unexpected error during creation: {e}")

    print()

    starter_deck = Deck()

    try:
        for c in cards_list:
            starter_deck.add_card(c)

        stats = starter_deck.get_deck_stats()
        print(f"Deck Stats: {stats}")
        starter_deck.shuffle()

    except Exception as e:
        print(f"[CRITICAL] Error managing deck: {e}")
        return

    print()
    print("Drawing and playing cards:")

    for i in range(1, 4):
        try:
            print()
            drew: Optional[Card] = starter_deck.draw_card()
            print(f"Drew: {drew.name}")

            play_result = drew.play({"available_mana": 10})
            print(f"Play result: {play_result}")

        except IndexError:
            print(f"Draw {i}: Cannot draw, deck is empty (IndexError).")
            break
        except Exception as e:
            print(f"Draw {i}: Error interacting with card: {e}")

    print()
    print("Polymorphism in action: Same interface, different card behaviors")


if __name__ == "__main__":
    main()
