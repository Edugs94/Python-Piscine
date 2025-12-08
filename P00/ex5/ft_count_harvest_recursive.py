def ft_count_harvest_recursive():
    days_total = int(input("Days until harvest: "))

    def count_days(current, max):
        if current > max:
            if max > 0:
                print("Harvest time!")
            return
        print(f"Day {current}")
        count_days(current + 1, max)
    count_days(1, days_total)
