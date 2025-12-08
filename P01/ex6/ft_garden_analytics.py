class Plant:
    def __init__(self, name: str, height: int, age: int):
        self.name = name
        self.height = height
        self.age = age

    def grow(self, centimeters: int) -> None:
        self.height += centimeters
        print(f"{self.name} grew {centimeters}cm")


class FloweringPlant(Plant):
    def __init__(self, name: str, height: int, age: int, color: str):
        super().__init__(name, height, age)
        self.color = color


class PrizeFlower(FloweringPlant):
    def __init__(self, name: str, height: int, age: int,
                 color: str, points: int):
        super().__init__(name, height, age, color)
        self.prize_points = points


class GardenManager:
    total_gardens = 0

    class GardenStats:

        def calculate_score(self, plants: list[Plant]) -> int:

            score = 0
            for plant in plants:
                score += plant.height
                if (isinstance(plant, FloweringPlant)):
                    score += 20
            return score

        def count_types(self, plants: list[Plant]) -> dict[str, int]:
            counts = {"regular": 0, "flowering": 0, "prize": 0}
            for plant in plants:
                if isinstance(plant, PrizeFlower):
                    counts["prize"] += 1
                elif isinstance(plant, FloweringPlant):
                    counts["flowering"] += 1
                else:
                    counts["regular"] += 1
            return counts

    def __init__(self, owner_name: str):
        self.owner_name = owner_name
        self.plants: list[Plant] = []
        self.total_growth_tracked = 0
        self.stats = self.GardenStats()
        GardenManager.total_gardens += 1

    def add_plant(self, plant: Plant) -> None:
        self.plants.append(plant)
        print(f"Added {plant.name} to {self.owner_name}'s garden")

    def grow_all_plants(self, centimeters: int) -> None:
        print(f"{self.owner_name} is helping all plants grow...")
        for plant in self.plants:
            plant.grow(centimeters)
            self.total_growth_tracked += centimeters

    def get_report(self) -> None:
        print(f"=== {self.owner_name}'s Garden Report ===")
        print("Plants in garden:")
        count = 0
        for plant in self.plants:
            count += 1
            output = f"{plant.name}: {plant.height}cm"

            if isinstance(plant, FloweringPlant):
                output += f", {plant.color} flowers (blooming)"

            if isinstance(plant, PrizeFlower):
                output += f", Prize points: {plant.prize_points}"
            print(output)

        print(f"Plants added: {count}, "
              f"Total growth: {self.total_growth_tracked}cm")

        types = self.stats.count_types(self.plants)
        print(f"Plant types: {types['regular']} regular, "
              f"{types['flowering']} flowering, "
              f"{types['prize']} prize flowers")

    @staticmethod
    def validate_height(height: int) -> bool:
        if height > 0:
            return True
        else:
            return False

    @classmethod
    def create_garden_network(cls) -> None:
        print(f"Total gardens managed: {cls.total_gardens}")


if __name__ == "__main__":
    print("=== Garden Management System Demo ===")
    print()

    alice_garden = GardenManager("Alice")
    alice_garden.add_plant(Plant("Oak Tree", 100, 365))
    alice_garden.add_plant(FloweringPlant("Rose", 25, 30, "red"))
    alice_garden.add_plant(PrizeFlower("Sunflower", 50, 45, "yellow", 10))
    print()
    alice_garden.grow_all_plants(1)
    print()

    alice_garden.get_report()
    print()

    print(f"Height validation test: {GardenManager.validate_height(101)}")
    bob_garden = GardenManager("Bob")
    bob_p1 = Plant("Oak Tree", 92, 10)
    bob_garden.add_plant(bob_p1)

    alice_score = alice_garden.stats.calculate_score(alice_garden.plants)
    bob_score = bob_garden.stats.calculate_score(bob_garden.plants)

    print(f"Garden scores Alice: {alice_score}, Bob: {bob_score}")

    GardenManager.create_garden_network()
