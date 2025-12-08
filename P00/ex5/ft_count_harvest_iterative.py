def ft_count_harvest_iterative():
    i = 1
    days_str = input("Days until harvest: ")
    days = int(days_str)
    while (i <= days):
        print(f"Day {i}")
        i += 1
    print("Harvest time!")
