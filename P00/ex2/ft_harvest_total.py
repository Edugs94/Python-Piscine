def ft_harvest_total():
    day1_str = input("Day 1 harvest: ")
    day2_str = input("Day 2 harvest: ")
    day3_str = input("Day 3 harvest: ")
    total = int(day1_str) + int(day2_str) + int(day3_str)
    print(f"Total harvest: {total}")
