from abc import ABC, abstractmethod
from typing import Any


class Combatable(ABC):
    """
    Abstract interface for engaging entities in combat.
    """

    @abstractmethod
    def attack(self, target: Any) -> dict[Any, Any]:
        """
        Execute an attack action against a specific target.
        """
        pass

    @abstractmethod
    def defend(self, incoming_damage: int) -> dict[Any, Any]:
        """
        Process defensive maneuvers or damage calculation against an attack.
        """
        pass

    @abstractmethod
    def get_combat_stats(self) -> dict[Any, Any]:
        """
        Retrieve the current combat statistics of the entity.
        """
        pass
