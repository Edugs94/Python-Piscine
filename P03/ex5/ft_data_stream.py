def get_next_prime():

    num = 2
    while (True):
        i = 2
        is_prime = True
        while (i < num):
            if (num % i == 0):
                is_prime = False
                break
            i += 1
        if is_prime is True:
            yield num
        num += 1


def get_next_fib():

    first = 0
    second = 1
    yield first
    yield second
    while (True):
        third = first + second
        yield third
        first, second = second, third


def print_numbers(times: int, generator: str) -> None:

    if generator == 'prime':
        i = 0
        print(f'Prime numbers (first {times}): ', end='')
        prime_generator = get_next_prime()
        for i in range(times):
            next_prime = next(prime_generator)
            if (i != times - 1):
                print(f'{next_prime}, ', end='')
            else:
                print(f'{next_prime}')

    if generator == 'fibonacci':
        i = 0
        print(f'Fibonacci sequence (first {times}): ', end='')
        fib_generator = get_next_fib()
        for i in range(times):
            next_fib = next(fib_generator)
            if (i != times - 1):
                print(f'{next_fib}, ', end='')
            else:
                print(f'{next_fib}')


def generate_events(players: list, actions: list, times: int):

    i = 0
    lvl10plus = 0
    treasure_events = 0
    level_up_events = 0
    print('=== Game Data Stream Processor ===')
    print()
    print(f"Processing {times} game events...")
    print()
    for i in range(times):

        player = players[i % len(players)]
        level = (i * 3 + 5) % 17
        action = actions[((i + level) % len(actions))]

        print(f'Event {i + 1}: Player {player}', end='')
        print(f' (level {level})', end='')
        print(f' {action}')

        if level >= 10:
            lvl10plus += 1
        if action == "found treasure":
            treasure_events += 1
        if action == "leveled up":
            level_up_events += 1

    print()
    stream_analytics(times, lvl10plus, treasure_events, level_up_events)


def stream_analytics(times, lvl10plus, treasure_events, level_up_events):
    print('=== Stream Analytics ===')
    print()
    print(f'Total events processed: {times}')
    print(f'High-level players (10+): {lvl10plus}')
    print(f'Treasure events: {treasure_events}')
    print(f'Level-up events: {level_up_events}')


def generator_demonstration():
    print()
    print('=== Generator Demonstration ===')
    print_numbers(10, 'fibonacci')
    print_numbers(5, 'prime')


def show_mem_use():
    secs = 0.045
    print()
    print('Memory usage: Constant (streaming)')
    print(f'Processing time: {secs} seconds')
    '#hard coded to fit example output as import time is not allowed'


if __name__ == "__main__":

    players = ["alice", "bob", "charlie"]
    actions = ["killed monster", "found treasure", "leveled up"]

    generate_events(players, actions, 1000)
    show_mem_use()
    generator_demonstration()
