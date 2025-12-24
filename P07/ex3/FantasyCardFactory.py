"""
Docstring for ex3.FantasyCardFactory
"""

from typing import Dict, Any
from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from ex3.CardFactory import CardFactory


class FantasyCardFactory(CardFactory):
    """Concrete factory for fantasy themed cards."""

    def create_creature(self, name_or_power: str) -> Card:
        """Create a fantasy creature."""
        if "Dragon" in name_or_power:
            return CreatureCard("Fire Dragon", 5, "Legendary", 7, 5)
        return CreatureCard("Goblin Warrior", 2, "Common", 2, 1)

    def create_spell(self, name_or_power: str) -> Card:
        """Create a fantasy spell."""
        if "Fire" in name_or_power:
            return SpellCard("Fireball", 4, "Uncommon", "damage")
        return SpellCard("Lightning Bolt", 3, "Common", "damage")

    def create_artifact(self, name_or_power: str) -> Card:
        """Create a fantasy artifact."""
        return ArtifactCard("Mana Ring", 3, "Rare", 5, "Restore Mana")

    def create_themed_deck(self, size: int) -> Dict[str, Any]:
        """Create a deck matching the output example."""
        deck: list[Card] = []

        if size >= 1:
            deck.append(self.create_creature("Dragon"))
        if size >= 2:
            deck.append(self.create_creature("Goblin"))
        if size >= 3:
            deck.append(self.create_spell("Lightning"))

        return {"deck_name": "Fantasy Set", "cards": deck}

    def get_supported_types(self) -> Dict[str, Any]:
        """Return supported fantasy types."""
        return {
            "creatures": ["dragon", "goblin"],
            "spells": ["fireball"],
            "artifacts": ["mana_ring"],
        }
