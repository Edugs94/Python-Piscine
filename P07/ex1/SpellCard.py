"""
Docstring for ex1.SpellCard
"""

from ex0.Card import Card
from ex0.CreatureCard import CreatureCard as Creature
from typing import Dict, Any


class UnknownEffect(Exception):
    pass


class SpellCard(Card):
    """
    Docstring for SpellCard
    """

    TYPE_ALIAS = "Spell"

    def __init__(
        self, name: str, cost: int, rarity: str, effect_type: str
    ) -> None:
        """
        Docstring for __init__
        """
        super().__init__(name, cost, rarity)
        self.effect_type = effect_type
        if self.effect_type not in ["damage", "heal", "buff", "debuff"]:
            raise UnknownEffect('Spell effect not found in game parameters')

    def play(self, game_state: Dict[str, Any]) -> Dict[str, Any]:
        """
        Docstring for play
        """
        available_mana: int = game_state.get("available_mana", 0)
        if self.is_playable(available_mana):
            data: Dict[Any, Any] = {
                "card_played": self.name,
                "mana_used": self.cost,
                "effect": self.resolve_effect([])["effect"],
            }
        else:
            data: Dict[Any, Any] = {
                "card_played": None,
                "mana_used": 0,
                "effect": None,
            }
        return data

    def resolve_effect(self, targets: list[Creature]) -> dict[str, Any]:
        description = "Unknown effect"
        if self.effect_type == "damage":
            description = "Deal 3 damage to target"
        elif self.effect_type == "heal":
            description = "Heal 3 points"
        elif self.effect_type == "buff":
            description = "Boost stats"

        return {"effect": description, "target": targets}
