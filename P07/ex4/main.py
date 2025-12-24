"""
Docstring for ex4.main
"""

from ex4.TournamentCard import TournamentCard
from ex4.TournamentPlatform import TournamentPlatform


def main():
    """Execute the tournament platform demonstration."""
    print("=== DataDeck Tournament Platform ===")

    platform = TournamentPlatform()

    print("\nRegistering Tournament Cards...")
    dragon = TournamentCard("Dragon", 5, "Legendary", 7, 5)
    wizard = TournamentCard("Wizard", 4, "Rare", 3, 4)

    id_dragon = platform.register_card(dragon)
    id_wizard = platform.register_card(wizard)

    for card, card_id in [(dragon, id_dragon), (wizard, id_wizard)]:
        print(f"{card.name} (ID: {card_id}):")
        print("Interfaces: ['Card', 'Combatable', 'Rankable']")
        print(f"Rating: {card.rating}")
        print(f"Record: {card.wins}-{card.losses}")

    print("\nCreating tournament match...")
    match_result = platform.create_match(id_dragon, id_wizard)
    print(f"Match result: {match_result}")

    print("\nTournament Leaderboard:")
    leaderboard = platform.get_leaderboard()
    for index, entry in enumerate(leaderboard, 1):
        print(f"{index}. {entry}")

    print("\nPlatform Report:")
    report = platform.generate_tournament_report()
    print(report)

    print("\n=== Tournament Platform Successfully Deployed! ===")
    print("All abstract patterns working together harmoniously!")


if __name__ == "__main__":
    main()
