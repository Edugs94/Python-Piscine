"""
Docstring for ex2.EliteCard
"""

from typing import Any, List, Dict
from ex0.Card import Card
from ex2.Combatable import Combatable
from ex2.Magical import Magical


class EliteCard(Card, Combatable, Magical):
    """
    A card type that combines physical combat and magical abilities.
    """

    def __init__(self, name: str, cost: int, rarity: str,
                 attack_power: int, health: int, mana: int):
        """
        Initialize an EliteCard with card details and combat/magic stats.
        """
        super().__init__(name, cost, rarity)
        self.attack_power = attack_power
        self.health = health
        self.mana = mana
        self.max_mana = mana

    @property
    def attack_power(self) -> int:
        """Get the attack power."""
        return self._attack_power

    @attack_power.setter
    def attack_power(self, value: int):
        """Set the attack power, ensuring it is positive."""
        if value <= 0:
            raise ValueError("Attack power must be greater than 0")
        self._attack_power = value

    @property
    def health(self) -> int:
        """Get the current health."""
        return self._health

    @health.setter
    def health(self, value: int):
        """Set the health, ensuring it is positive."""
        if value <= 0:
            raise ValueError("Health must be greater than 0")
        self._health = value

    def play(self, game_state: Dict[str, Any]) -> Dict[str, Any]:
        """
        Play the elite card onto the battlefield.
        """
        available_mana: int = game_state.get("available_mana", 0)
        if self.is_playable(available_mana):
            data: Dict[str, Any] = {
                "card_played": self.name,
                "mana_used": self.cost,
                "effect": "Elite unit summoned with combat and magic skills",
            }
        else:
            data: Dict[str, Any] = {
                "card_played": None,
                "mana_used": 0,
                "effect": None,
            }
            raise Exception("Not enough mana")
        return data

    def attack(self, target: Any) -> Dict[str, Any]:
        """
        Perform a physical attack on a target.
        """
        return {
            "attacker": self.name,
            "target": str(target),
            "damage": self.attack_power,
            "combat_type": "melee",
        }

    def defend(self, incoming_damage: int) -> Dict[str, Any]:
        """
        Absorb damage and update health status.
        Handles the edge case where damage reduces health <= 0.
        """
        try:
            self.health -= incoming_damage
            alive = True
        except ValueError:
            self._health = 0
            alive = False

        return {
            "defender": self.name,
            "damage_taken": incoming_damage,
            "remaining_health": self._health,
            "still_alive": alive,
        }

    def get_combat_stats(self) -> Dict[str, Any]:
        """
        Get current combat-related statistics.
        """
        return {"attack": self.attack_power, "health": self._health}

    def cast_spell(
        self, spell_name: str, targets: List[str]
    ) -> Dict[str, Any]:
        """
        Cast a magic spell if sufficient mana is available.
        """
        spell_cost = 10
        if self.mana >= spell_cost:
            self.mana -= spell_cost
            return {
                "caster": self.name,
                "spell": spell_name,
                "targets": [str(t) for t in targets],
                "mana_used": spell_cost,
            }
        return {
            "caster": self.name,
            "error": "Insufficient mana",
            "required": spell_cost,
            "current": self.mana,
        }

    def channel_mana(self, amount: int) -> Dict[str, Any]:
        """
        Recover mana points.
        """
        self.mana += amount
        return {"channeled": amount, "total_mana": self.mana}

    def get_magic_stats(self) -> Dict[str, Any]:
        """
        Get current magic-related statistics.
        """
        return {
            "mana": self.mana,
            "spell_power": "High",
        }
