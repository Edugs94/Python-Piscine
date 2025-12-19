"""
Docstring for ex1.Deck
"""

from typing import Any
from ex0.Card import Card
from ex0.CreatureCard import CreatureCard as Creature
from ex1.ArtifactCard import ArtifactCard as Artifact
from ex1.SpellCard import SpellCard as Spell
import random


class EmptyDeck(Exception):
    pass


class Deck:
    """
    Docstring for Deck
    """

    def __init__(self) -> None:
        """
        Docstring for __init__
        """
        self.cards: list[Card] = []

    def add_card(self, card: Card) -> None:
        """
        Docstring for add_card
        """
        self.cards.append(card)

    def remove_card(self, card_name: str) -> bool:
        """
        Docstring for remove_card
        """
        for card in self.cards:
            if card_name == card.name:
                self.cards.remove(card)
                return True
        return False

    def shuffle(self) -> None:
        """
        Docstring for shuffle
        """
        random.shuffle(self.cards)

    def draw_card(self) -> Card:
        """
        Docstring for draw_card
        """
        if not self.cards:
            raise EmptyDeck("No cards to be drawn. Deck empty")
        return self.cards.pop()

    def get_deck_stats(self) -> dict[str, Any]:
        """
        Get total_cards in deck, count of each type and average cost
        """
        if not self.cards:
            raise EmptyDeck("No cards in deck")
        info: dict[str, Any] = {
            "total_cards": len(self.cards),
            "creatures": sum(1 for c in self.cards if isinstance(c, Creature)),
            "spells": sum(1 for c in self.cards if isinstance(c, Spell)),
            "artifacts": sum(1 for c in self.cards if isinstance(c, Artifact)),
            "avg_cost": round(
                sum(c.cost for c in self.cards) / len(self.cards), 1
            ),
        }
        return info
