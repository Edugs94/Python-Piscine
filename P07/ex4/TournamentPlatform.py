"""
Docstring for ex4.TournamentPlatform
"""

from typing import Dict, List, Any
from ex4.TournamentCard import TournamentCard


class TournamentPlatform:
    """Manages tournament cards, matches, and ranking systems."""

    def __init__(self):
        """Initialize the platform with empty storage and match counters."""
        self.cards: Dict[str, TournamentCard] = {}
        self.matches_played: int = 0

    def register_card(self, card: TournamentCard) -> str:
        """Register a card and return a unique ID based on its name."""
        card_id = (
            f"{card.name.lower().replace(' ', '_')}_001"
        )
        self.cards[card_id] = card
        return card_id

    def create_match(self, card1_id: str, card2_id: str) -> Dict[str, Any]:
        """Execute a match between two cards and update their ratings."""
        fighter1 = self.cards[card1_id]
        fighter2 = self.cards[card2_id]
        fighter1.health, fighter2.health = (
            fighter1.max_health,
            fighter2.max_health,
        )
        winner: TournamentCard = None  # type: ignore
        loser: TournamentCard = None  # type: ignore

        while fighter1.health > 0 and fighter2.health > 0:
            fighter2.defend(fighter1.attack(fighter2)["damage_dealt"])
            if fighter2.health <= 0:
                winner, loser = fighter1, fighter2
                break
            fighter1.defend(fighter2.attack(fighter1)["damage_dealt"])
            if fighter1.health <= 0:
                winner, loser = fighter2, fighter1
                break

        if not winner:
            winner, loser = fighter1, fighter2

        winner.update_wins()
        loser.update_losses()
        self.matches_played += 1
        return {
            "winner": winner.name,
            "loser": loser.name,
            "winner_rating": winner.rating,
            "loser_rating": loser.rating,
        }

    def get_leaderboard(self) -> List[str]:
        """Return a list of card strings sorted
        by rating in descending order."""

        def get_rating(card: TournamentCard) -> int:
            """Return the card's rating for sorting."""
            return card.rating

        sorted_cards = sorted(
            self.cards.values(), key=get_rating, reverse=True
        )

        return [
            f"{c.name} - Rating: {c.rating} ({c.wins}-{c.losses})"
            for c in sorted_cards
        ]

    def generate_tournament_report(self) -> Dict[str, Any]:
        """Generate a dictionary with platform statistics and status."""
        total = sum(c.rating for c in self.cards.values())
        avg = total / len(self.cards) if self.cards else 0
        return {
            "total_cards": len(self.cards),
            "matches_played": self.matches_played,
            "avg_rating": avg,
            "platform_status": "active",
        }
