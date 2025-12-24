"""
Docstring for ex4.TournamentCard
"""

from typing import Any, Dict
from ex0.Card import Card
from ex2.Combatable import Combatable
from ex4.Rankable import Rankable


class TournamentCard(Card, Combatable, Rankable):
    """Represents a card capable of combat and
    ranking in a tournament system."""

    def __init__(
        self, name: str, cost: int, rarity: str, attack_power: int, health: int
    ):
        """Initialize the tournament card with basic stats, combat stats,
        and default ranking."""
        super().__init__(name, cost, rarity)
        self.attack_power = attack_power
        self.health = health
        self.max_health = health
        self.rating = 1000
        self.wins = 0
        self.losses = 0

    @property
    def health(self) -> int:
        """Get the current health."""
        return self._health

    @health.setter
    def health(self, value: int) -> None:
        """Set health, ensuring it never goes below 0."""
        self._health = max(0, value)

    @property
    def attack_power(self) -> int:
        """Get the current attack power."""
        return self._attack_power

    @attack_power.setter
    def attack_power(self, value: int) -> None:
        """Set attack power, ensuring it never goes below 0."""
        self._attack_power = max(0, value)

    def play(self, game_state: Dict[str, Any]) -> Dict[str, Any]:
        """Execute the card's play effect and return the result."""
        return {
            "card_played": self.name,
            "effect": "Entered the tournament arena",
        }

    def get_card_info(self) -> Dict[str, Any]:
        """Return a dictionary containing the card's
        basic and combat information."""
        return {
            "name": self.name,
            "cost": self.cost,
            "rarity": self.rarity,
            "attack": self.attack_power,
            "health": self.health,
        }

    def is_playable(self, available_mana: int) -> bool:
        """Check if the card can be played with the available mana."""
        return self.cost <= available_mana

    def attack(self, target: Any) -> Dict[str, Any]:
        """Perform an attack on a target and return the combat result."""
        return {"attacker": self.name, "damage_dealt": self.attack_power}

    def defend(self, incoming_damage: int) -> Dict[str, Any]:
        """Process incoming damage and update the card's health."""
        self.health -= incoming_damage

        return {
            "defender": self.name,
            "damage_taken": incoming_damage,
            "health_remaining": self.health,
        }

    def get_combat_stats(self) -> Dict[str, Any]:
        """Return the current combat statistics of the card."""
        return {"attack": self.attack_power, "health": self.health}

    def calculate_rating(self) -> int:
        """Return the current tournament rating (ELO)."""
        return self.rating

    def update_wins(self, wins: int = 1) -> None:
        """Update the win count and increase the rating."""
        self.wins += wins
        self.rating += 10 * wins

    def update_losses(self, losses: int = 1) -> None:
        """Update the loss count and decrease the rating."""
        self.losses += losses
        self.rating -= 10 * losses

    def get_rank_info(self) -> Dict[str, Any]:
        """Return the current ranking statistics
        including rating and record."""
        return {
            "rating": self.rating,
            "wins": self.wins,
            "losses": self.losses,
        }

    def get_tournament_stats(self) -> Dict[str, Any]:
        """Aggregate and return all card, combat, and ranking statistics."""
        return {
            "card_info": self.get_card_info(),
            "combat_stats": self.get_combat_stats(),
            "rank_stats": self.get_rank_info(),
        }
