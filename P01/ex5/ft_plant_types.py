class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age


class Flower(Plant):
    def __init__(self, name, height, age, color):
        super().__init__(name, height, age)
        self.color = color

    def bloom(self):
        print(f"{self.name} is blooming beautifully!")


class Tree(Plant):
    def __init__(self, name, height, age, trunk_diameter):
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self):
        print(f"{self.name} provides {int(self.trunk_diameter * 1.56)} square"
              " meters of shade")


class Vegetable(Plant):
    def __init__(self, name, height, age, harvest_season, nutritional_value):
        super().__init__(name, height, age)
        self.nutritional_value = nutritional_value
        self.harvest_season = harvest_season

    def display_nutritional_info(self):
        print(f"{self.name} is rich in {self.nutritional_value}")


def ft_plant_types():
    print("=== Garden Plant Types ===")
    print()
    data_plants = [
        Flower("Rose", 25, 30, "red"),
        Flower("Tulip", 20, 45, "white"),
        Tree("Oak", 500, 1825, 50),
        Tree("Pine", 700, 1950, 100),
        Vegetable("Tomato", 80, 90, "summer", "vitamin C"),
        Vegetable("Cucumber", 80, 90, "fall", "magnesium"),
    ]
    i = 0
    while i < 6:
        plant = data_plants[i]
        print(f"{plant.name} ({plant.__class__.__name__}): "
              f"{plant.height}cm, {plant.age} days, ", end="")
        if plant.__class__.__name__ == "Flower":
            print(f"{plant.color} color")
            plant.bloom()
        elif plant.__class__.__name__ == "Tree":
            print(f"{plant.trunk_diameter}cm diameter")
            plant.produce_shade()
        elif plant.__class__.__name__ == "Vegetable":
            print(f"{plant.harvest_season} harvest")
            plant.display_nutritional_info()
        if i != 5:
            print()
        i += 1
