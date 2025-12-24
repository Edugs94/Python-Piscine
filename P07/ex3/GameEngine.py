from typing import Dict, Any, List, Optional
from ex3.GameStrategy import GameStrategy
from ex3.CardFactory import CardFactory


class GameEngine:
    """Orchestrates the game flow using factory and strategy."""

    def __init__(self) -> None:
        """Initialize the engine."""
        self.factory: Optional[CardFactory] = None
        self.strategy: Optional[GameStrategy] = None
        self.hand: List[Any] = []
        self.battlefield: List[Any] = []

    def configure_engine(
        self, factory: CardFactory, strategy: GameStrategy
    ) -> None:
        """Set up the engine components."""
        self.factory = factory
        self.strategy = strategy
        deck_data = self.factory.create_themed_deck(3)
        self.hand = deck_data["cards"]

    def simulate_turn(self) -> Dict[str, Any]:
        """Execute a turn simulation."""
        if not self.strategy or not self.factory:
            raise ValueError("Engine not configured")

        turn_result: Any = self.strategy.execute_turn(
            self.hand, self.battlefield
        )

        return {
            "strategy": self.strategy.get_strategy_name(),
            "actions": turn_result,
        }

    def get_engine_status(self) -> Dict[str, Any]:
        """Return current engine state."""
        return {
            "factory": type(self.factory).__name__,
            "strategy": (
                self.strategy.get_strategy_name() if self.strategy else "None"
            ),
            "hand_size": len(self.hand),
        }
