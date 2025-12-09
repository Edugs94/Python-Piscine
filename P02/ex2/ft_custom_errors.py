class GardenError(Exception):
    """Base exception class for all garden-related errors."""
    pass


class PlantError(GardenError):
    """Exception raised for issues specific to plant health."""
    pass


class WaterError(GardenError):
    """Exception raised for issues related to water supply."""
    pass


def check_plant(plant, plant_status):
    """Verifies plant health and raises PlantError if the plant is wilting."""

    if plant_status == 'wilting':
        raise PlantError("The tomato plant is wilting!")
    print(f"The {plant} seems to be ok")


def check_tank(tank_status):
    """Checks tank water level and raises WaterError if empty."""

    if tank_status == "empty":
        raise WaterError("Not enough water in the tank!")
    print("Tank has enough water")


def custom_errors():
    """Demonstrates catching specific and general custom garden exceptions."""

    print('=== Custom Garden Errors Demo ===')
    print()

    print('Testing PlantError...')
    try:
        check_plant('tomato', 'wilting')
    except PlantError as e:
        print('Caught PlantError: ', end='')
        print(e)
    print()

    print('Testing WaterError...')
    try:
        check_tank('empty')
    except WaterError as e:
        print('Caught WaterError: ', end='')
        print(e)
    print()

    print('Testing catching all garden errors...')
    try:
        check_plant('tomato', 'wilting')
    except GardenError as e:
        print(f"Caught a garden error: {e}")

    try:
        check_tank('empty')
    except GardenError as e:
        print(f"Caught a garden error: {e}")
    print()
    print("All custom error types work correctly!")


if __name__ == "__main__":
    custom_errors()
