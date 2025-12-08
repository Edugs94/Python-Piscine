def ft_water_reminder():
    days_str = input("Days since last watering: ")
    days = int(days_str)
    if (days > 2):
        print("Water the plants!")
    else:
        print("Plants are fine")
