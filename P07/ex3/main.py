from ex3.FantasyCardFactory import FantasyCardFactory
from ex3.AggressiveStrategy import AggressiveStrategy
from ex3.GameEngine import GameEngine
from typing import Any


def main() -> None:
    """Demonstrate the Abstract Factory and Strategy patterns."""
    print("=== DataDeck Game Engine ===\n")

    print("Configuring Fantasy Card Game...")
    factory = FantasyCardFactory()
    strategy = AggressiveStrategy()
    engine = GameEngine()

    engine.configure_engine(factory, strategy)

    print(f"Factory: {type(factory).__name__}")
    print(f"Strategy: {strategy.get_strategy_name()}")

    supported_types = factory.get_supported_types()
    print(f"Available types: {supported_types}\n")

    print("Simulating aggressive turn...")

    hand_descriptions = [
        f"{card.name} ({card.cost})"
        for card in engine.hand
        if hasattr(card, "cost")
    ]
    print(f"Hand: {hand_descriptions}\n")

    turn_result = engine.simulate_turn()

    print("Turn execution:")
    print(f"Strategy: {turn_result['strategy']}")
    print(f"Actions: {turn_result['actions']}\n")

    game_report: dict[str, Any] = {
        "turns_simulated": 1,
        "strategy_used": strategy.get_strategy_name(),
        "total_damage": turn_result["actions"].get("damage_dealt", 0),
        "cards_created": len(engine.hand),
    }
    print("Game Report:")
    print(game_report)

    print(
        "\nAbstract Factory + Strategy Pattern: Maximum flexibility achieved!"
    )


if __name__ == "__main__":
    main()
