"""
Docstring for alchemy.grimoire.spellbook
"""


def record_spell(spell_name: str, ingredients: str) -> str:
    '''
    Returns if a spell can be recorded or not based on its
    ingredients
    '''
    from alchemy.grimoire.validator import validate_ingredients

    validation = validate_ingredients(ingredients)
    if validation == f"{ingredients} - INVALID":
        return (
            "Spell rejected: "
            f"{spell_name} ({validation})"
        )
    return (
        "Spell recorded: " f"{spell_name} ({validation})"
    )
