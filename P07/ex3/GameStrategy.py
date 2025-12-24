from abc import ABC, abstractmethod
from typing import List, Dict, Any


class GameStrategy(ABC):
    """Abstract interface for game strategies."""

    @abstractmethod
    def execute_turn(
        self, hand: List[Any], battlefield: List[Any]
    ) -> Dict[str, Any]:
        """Execute a turn based on the strategy."""
        pass

    @abstractmethod
    def get_strategy_name(self) -> str:
        """Return the strategy name."""
        pass

    @abstractmethod
    def prioritize_targets(self, available_targets: List[Any]) -> List[Any]:
        """Return a list of targets sorted by priority."""
        pass
