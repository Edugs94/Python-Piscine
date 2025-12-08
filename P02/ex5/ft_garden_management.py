class GardenError(Exception):
    pass


class EmptyName(GardenError):
    pass


class HealthError(GardenError):
    pass


class WaterError(GardenError):
    pass


class GardenManager:

    valid_plants = []

    def add_plants(plant):
        if plant is None:
            raise EmptyName("Error adding plant: Plant name cannot be empty!")
        GardenManager.valid_plants.append(plant)
        print(f'Added {plant[0]} successfully')

    def water_plants(valid_plants):
        for plant in GardenManager.valid_plants:
            try:
                print(f'Watering {plant[0]} - success')
            except EmptyName as e:
                print(e)
        print('Closing watering system (cleanup)')

    def check_health(plant_name, water_level, sunlight_hours):

        if not plant_name:
            raise HealthError("Error: Plant name cannot be empty!")

        if water_level < 1:
            raise HealthError(f"Error checking {plant_name}: Water level"
                              f" {water_level} is too low (min 1)")
        if water_level > 10:
            raise HealthError(f"Error checking {plant_name}: Water level"
                              f" {water_level} is too high (max 10)")

        if sunlight_hours < 2:
            raise HealthError(f"Error checking {plant_name}: Sunlight hours"
                              f" {sunlight_hours} is too low (min 2)")
        if sunlight_hours > 12:
            raise HealthError(f"Error checking {plant_name}: Sunlight hours"
                              f" {sunlight_hours} is too high (max 12)")
        print(f"{plant_name}: healthy (water: {water_level},"
              f" sun: {sunlight_hours})")

    def check_tank(tank_status):
        if tank_status == "empty":
            raise WaterError("Caught GardenError: "
                             "Not enough water in the tank")

    def get_report(plant_list, tank_status):
        print('=== Garden Management System ===')
        print()
        print('Adding plants to garden...')
        for plant in plant_list:
            try:
                GardenManager.add_plants(plant)
            except EmptyName as e:
                print(e)
        print()
        print('Watering plants...')
        print('Opening watering system')
        GardenManager.water_plants(GardenManager.valid_plants)
        print()

        print('Checking plant health...')
        try:
            for plant in GardenManager.valid_plants:
                GardenManager.check_health(plant[0], plant[1], plant[2])
        except HealthError as e:
            print(e)
        print()

        print('Testing error recovery...')
        try:
            GardenManager.check_tank(tank_status)
        except GardenError as e:
            print(e)
        finally:
            print('System recovered and continuing...')

        print()
        print('Garden management system test complete!')


GardenManager.get_report([('tomato', 5, 8), ('lettuce', 15, 8), None], 'empty')
