class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def display_info(self):
        print(f"Created: {self.name} ({self.height}cm, {self.age} days)")


def ft_plant_factory():
    plant_data = [
        ("Rose", 25, 30),
        ("Oak", 200, 365),
        ("Cactus", 5, 90),
        ("Sunflower", 80, 45),
        ("Fern", 15, 120)
    ]
    print("=== Plant Factory Output ===")
    i = 0
    while (i < 5):
        data_plant = plant_data[i]
        new_plant = Plant(*data_plant)
        new_plant.display_info()
        i += 1
    print(f"Total plants created: {i}")
