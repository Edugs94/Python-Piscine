class WrongPlant(Exception):
    """Exception raised when a plant is invalid or None."""
    pass


def watering_plant(plant):
    """Waters a specific plant or raises an error if the plant is None."""
    if plant is None:
        raise WrongPlant('Error: Cannot water None - invalid plant!')
    print(f'Watering {plant}')


def water_plants(plant_list):
    """Waters a list of plants, ensuring the
    system closes via a finally block."""
    print('Opening watering system')
    try:
        for plant in plant_list:
            watering_plant(plant)
    except WrongPlant as e:
        print(e)
        return
    finally:
        print('Closing watering system (cleanup)')
    print('Watering completed successfully!')


def test_watering_system():
    """Tests the watering system with valid
    and invalid lists to verify cleanup."""

    print('=== Garden Watering System ===')
    print()
    plant_list = ['tomato', 'lettuce', 'carrots']
    wrong_list = ['tomato', None, 'carrots']
    print('Testing normal watering...')
    water_plants(plant_list)
    print()
    print('Testing with error...')
    water_plants(wrong_list)
    print()
    print('Cleanup always happens, even with errors!')


if __name__ == "__main__":
    test_watering_system()
