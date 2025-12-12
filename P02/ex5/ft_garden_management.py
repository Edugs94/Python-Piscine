class GardenError(Exception):
    """Base exception class for all garden-related errors."""
    pass


class EmptyName(GardenError):
    """Exception raised when a plant name is missing"""
    pass


class HealthError(GardenError):
    """Exception raised for invalid plant health metrics."""
    pass


class WaterError(GardenError):
    """Exception raised for water tank issues."""
    pass


class GardenManager:
    """Manages garden operations including planting,
    watering, and monitoring."""

    def __init__(self):
        self.valid_plants = []

    def add_plants(self, plant):
        """Adds a plant to the manager or raises error if the plant is None."""

        if plant is None:
            raise EmptyName("Error adding plant: Plant name cannot be empty!")
        self.valid_plants.append(plant)
        print(f'Added {plant[0]} successfully')

    def water_plants(self):
        """Iterates through valid plants to simulate watering."""

        print('Opening watering system')
        for plant in self.valid_plants:
            print(f'Watering {plant[0]} - success')
        print('Closing watering system (cleanup)')

    def check_health(self, plant_name, water_level, sunlight_hours):
        """Validates water and sunlight levels,
        raising errors if out of range."""

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

    def check_tank(self, tank_status):
        """Checks the water tank status and raises an error if empty."""

        if tank_status == "empty":
            raise WaterError("Caught GardenError: "
                             "Not enough water in the tank")

    def test_garden_management(self, plant_list, tank_status):
        """Executes the full garden simulation workflow."""

        print('=== Garden Management System ===')
        print()
        print('Adding plants to garden...')
        for plant in plant_list:
            try:
                self.add_plants(plant)
            except EmptyName as e:
                print(e)
        print()

        print('Watering plants...')
        self.water_plants()
        print()

        print('Checking plant health...')
        try:
            for plant in self.valid_plants:
                self.check_health(*plant)
        except HealthError as e:
            print(e)
        print()

        print('Testing error recovery...')
        try:
            self.check_tank(tank_status)
        except GardenError as e:
            print(e)
        finally:
            print('System recovered and continuing...')

        print()
        print('Garden management system test complete!')


if __name__ == "__main__":
    manager = GardenManager()
    manager.test_garden_management([('tomato', 5, 8),
                        ('lettuce', 15, 8), None], 'empty')
