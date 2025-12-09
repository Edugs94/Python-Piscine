class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def grow(self, days, growth_rate):
        growth_amount = days * growth_rate
        self.height += growth_amount
        return growth_amount

    def age_increase(self, days):
        self.age += days

    def get_info(self, days, growth_amount):

        print(f"=== Day {days + 1} ===")
        print(f"{self.name}: {self.height}cm, {self.age} days old")
        if days != 0:
            print(f"Growth this week: +{growth_amount}cm")


rose = Plant("Rose", 25, 30)
sunflower = Plant("Sunflower", 80, 45)
cactus = Plant("Cactus", 15, 120)


def ft_plant_growth(plant, growth_rate):
    plant.get_info(0, 0)
    days_to_simulate = 6
    growth = plant.grow(days_to_simulate, growth_rate)
    plant.age_increase(days_to_simulate)
    plant.get_info(6, growth)


if __name__ == "__main__":
    ft_plant_growth(rose, 1)
