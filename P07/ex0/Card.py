"""
Docstring for ex0.Card
"""

from abc import ABC, abstractmethod
from typing import Any, Dict
from enum import Enum


class Rarity(str, Enum):
    COMMON = "Common"
    RARE = "Rare"
    EPIC = "Epic"
    LEGENDARY = "Legendary"


class Card(ABC):
    """
    Docstring for Card
    """

    TYPE_ALIAS = "Placeholder to be overwitten"

    def __init__(self, name: str, cost: int, rarity: str) -> None:
        """
        Docstring for __init__
        """
        super().__init__()
        self.name = name
        self.cost = cost
        self.rarity = rarity

    @abstractmethod
    def play(self, game_state: Dict[Any, Any]) -> Dict[Any, Any]:
        """
        Abstact method defined in cards subclasses
        """
        ...

    def get_card_info(self) -> Dict[Any, Any]:
        """
        Returns information of card selected
        """
        info: Dict[Any, Any] = {
            "name": self.name,
            "cost": self.cost,
            "rarity": self.rarity,
        }
        return info

    def is_playable(self, available_mana: int) -> bool:
        """
        Checks if available_mana >= self.cos
        """
        if available_mana >= self.cost:
            return True
        return False
