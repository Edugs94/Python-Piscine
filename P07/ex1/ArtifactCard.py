"""
Docstring for ex1.ArtifactCard
"""

from ex0.Card import Card
from typing import Dict, Any


class ArtifactCard(Card):
    """
    Docstring for Artifact
    """

    TYPE_ALIAS = "Artifact"

    def __init__(
        self, name: str, cost: int, rarity: str, durability: int, effect: str
    ) -> None:
        """
        Docstring for __init__
        """
        super().__init__(name, cost, rarity)
        self.durability = durability
        self.effect = effect

    def play(self, game_state: Dict[str, Any]) -> Dict[str, Any]:
        """
        Docstring for play
        """
        available_mana: int = game_state.get("available_mana", 0)
        if self.is_playable(available_mana):
            data: Dict[Any, Any] = {
                "card_played": self.name,
                "mana_used": self.cost,
                "effect": self.effect,
            }
        else:
            data: Dict[Any, Any] = {
                "card_played": None,
                "mana_used": 0,
                "effect": None,
            }
        return data

    def activate_ability(self) -> dict[str, Any]:
        """
        Docstring for activate_ability
        """
        result: dict[str, Any] = {
            "effect": self.effect,
            "resolved": True,
        }
        return result
