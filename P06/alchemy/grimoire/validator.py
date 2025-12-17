"""
Docstring for alchemy.grimoire.validator
"""


def validate_ingredients(ingredients: str) -> str:
    '''Validates if fire, water, wind or air are in ingredients'''
    if any(
        element in ingredients for element in ["fire", "water", "earth", "air"]
    ):
        return f"{ingredients} - VALID"
    else:
        return f"{ingredients} - INVALID"
