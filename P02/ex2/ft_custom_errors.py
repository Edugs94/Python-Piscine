class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


def check_plant(plant, plant_status):
    if plant_status == 'wilting':
        raise PlantError("Caught PlantError: The tomato plant is wilting!")
    print(f"The {plant} seems to be ok")


def check_tank(tank_status):
    if tank_status == "empty":
        raise WaterError("Caught WaterError: Not enough water in the tank!")
    print("Tank has enough water")


def custom_errors():

    print('=== Custom Garden Errors Demo ===')
    print()

    print('Testing PlantError...')
    try:
        check_plant('tomato', 'wilting')
    except PlantError as e:
        print(e)
    print()

    print('Testing WaterError...')
    try:
        check_tank('empty')
    except WaterError as e:
        print(e)
    print()

    print('Testing catching all garden errors...')
    try:
        check_plant('tomato', 'wilting')
    except PlantError as e:
        print(e)
    try:
        check_tank('empty')
    except GardenError as e:
        print(e)
