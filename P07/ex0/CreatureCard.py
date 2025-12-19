"""
Docstring for ex0.CreatureCard
"""

from __future__ import annotations
from ex0.Card import Card
from typing import Dict, Any


class CreatureCard(Card):
    """
    Docstring for CreatureCard
    """

    def __init__(
        self, name: str, cost: int, rarity: str, attack: int, health: int
    ) -> None:
        """
        Docstring for __init__
        """
        super().__init__(name, cost, rarity)
        self.attack = attack
        self.health = health

    @property
    def attack(self) -> int:
        """
        Docstring for attack encapsulation
        """
        return self._attack

    @property
    def health(self) -> int:
        """
        Docstring for health encapsulation
        """
        return self._health

    @attack.setter
    def attack(self, new_attack: int):
        """
        Protects attack from being less or equal than 0
        """
        if not isinstance(new_attack, int):  # type: ignore
            raise ValueError("Attack must be an int value")
        if new_attack <= 0:
            raise ValueError("Attack must be more than 0")
        self._attack: int = new_attack

    @health.setter
    def health(self, new_health: int):
        '''
        Protects health from being less or equal than 0
        '''
        if not isinstance(new_health, int):  # type: ignore
            raise ValueError("Health must be an int value")
        if new_health <= 0:
            raise ValueError("Health must be more than 0")
        self._health: int = new_health

    def play(self, game_state: Dict[Any, Any]) -> Dict[Any, Any]:
        """
        Docstring for play
        """
        available_mana = game_state.get("available_mana", 0)
        if self.is_playable(available_mana):
            data: Dict[Any, Any] = {
                "card_played": self.name,
                "mana_used": self.cost,
                "effect": "Creature summoned to battlefield",
            }
        else:
            data: Dict[Any, Any] = {
                "card_played": None,
                "mana_used": 0,
                "effect": None,
            }
        return data

    def get_card_info(self) -> Dict[Any, Any]:
        '''
        Adds specific info if card is creature to parent method
        '''
        info = super().get_card_info()
        info.update(
            {"attack": self.attack, "health": self.health, "type": "Creature"}
        )
        return info

    def attack_target(self, target: CreatureCard) -> dict[str, Any]:
        """
        Displays information:
        """
        result: dict[Any, Any] = {
            "attacker": self.name,
            "target": target.name,
            "damage_dealt": self._attack,
            "combat_resolved": True,
        }
        return result
