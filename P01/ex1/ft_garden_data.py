class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age


rose = Plant("Rose", 25, 30)
sunflower = Plant("Sunflower", 80, 45)
cactus = Plant("Cactus", 15, 120)


def ft_garden_data():
    print("=== Garden Plant Registry ===")
    print(f"{rose.name}: {rose.height}cm, {rose.age} days old")
    print(f"{sunflower.name}: {sunflower.height}cm, {sunflower.age} days old")
    print(f"{cactus.name}: {cactus.height}cm, {cactus.age} days old")


if __name__ == "__main__":
    ft_garden_data()
