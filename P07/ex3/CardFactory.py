'''
Docstring for ex3.CardFactory
'''
from abc import ABC, abstractmethod
from typing import Dict, Any
from ex0.Card import Card


class CardFactory(ABC):
    """Abstract factory interface for creating cards."""

    @abstractmethod
    def create_creature(self, name_or_power: str) -> Card:
        """Create a creature card."""
        pass

    @abstractmethod
    def create_spell(self, name_or_power: str) -> Card:
        """Create a spell card."""
        pass

    @abstractmethod
    def create_artifact(self, name_or_power: str) -> Card:
        """Create an artifact card."""
        pass

    @abstractmethod
    def create_themed_deck(self, size: int) -> Dict[str, Any]:
        """Create a complete themed deck."""
        pass

    @abstractmethod
    def get_supported_types(self) -> Dict[str, Any]:
        """Return supported card types."""
        pass
