def ft_plant_age():
    days_str = input("Enter plant age in days: ")
    days = int(days_str)
    if (days > 60):
        print("Plant is ready to harvest!")
    else:
        print("Plant needs more time to grow.")
