"""
Docstring for ex3.AggressiveStrategy
"""

from typing import List, Dict, Any
from ex3.GameStrategy import GameStrategy


class AggressiveStrategy(GameStrategy):
    """Concrete strategy focusing on damage and low cost."""

    def _get_card_cost(self, card: Any) -> int:
        """Helper to safely get card cost for sorting."""
        if hasattr(card, "cost"):
            return card.cost
        return 99

    def execute_turn(
        self, hand: List[Any], battlefield: List[Any]
    ) -> Dict[str, Any]:
        """Play low cost cards up to a mana limit."""
        actions: list[Any] = []
        mana_used = 0
        damage_dealt = 0
        available_mana = 6
        hand.sort(key=self._get_card_cost)

        for card in hand:
            if hasattr(card, "cost"):
                if mana_used + card.cost <= available_mana:
                    actions.append(card.name)
                    mana_used += card.cost

                    if hasattr(card, "attack"):
                        damage_dealt += card.attack
                    elif (
                        hasattr(card, "effect_type")
                        and card.effect_type == "damage"
                    ):
                        damage_dealt += 6
                else:
                    pass

        return {
            "cards_played": actions,
            "mana_used": mana_used,
            "targets_attacked": ["Enemy Player"],
            "damage_dealt": damage_dealt,
        }

    def get_strategy_name(self) -> str:
        """Return the strategy name."""
        return "AggressiveStrategy"

    def _get_target_health(self, target: Any) -> int:
        """Helper to get target health."""
        return target.health

    def prioritize_targets(self, available_targets: List[Any]) -> List[Any]:
        """Prioritize player and weak targets."""
        return sorted(available_targets, key=self._get_target_health)
