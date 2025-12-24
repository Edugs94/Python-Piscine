"""
Docstring for ex2.Magical
"""

from abc import ABC, abstractmethod
from typing import Any


class Magical(ABC):
    """Abstract interface for entities capable of using magic."""

    @abstractmethod
    def cast_spell(
        self, spell_name: str, targets: list[Any]
    ) -> dict[Any, Any]:
        """Cast a specific spell on the given targets."""
        pass

    @abstractmethod
    def channel_mana(self, amount: int) -> dict[Any, Any]:
        """Gain or manipulate a specific amount of mana."""
        pass

    @abstractmethod
    def get_magic_stats(self) -> dict[Any, Any]:
        """Retrieve the current magic statistics of the entity."""
        pass
