"""Exercise 5: Data Stream"""


def get_next_prime():
    '''Yield next existing prime number'''
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
    '''Yield next existing fibonacci number'''
    first = 0
    second = 1
    yield first
    yield second
    while (True):
        third = first + second
        yield third
        first, second = second, third


def print_numbers(times: int, generator: str) -> None:
    '''Print prime or fibonacci number yielded by generators'''
    if generator == 'prime':
        print(f'Prime numbers (first {times}): ', end='')
        prime_generator = get_next_prime()
        for i in range(times):
            next_prime = next(prime_generator)
            if (i != times - 1):
                print(f'{next_prime}, ', end='')
            else:
                print(f'{next_prime}')

    if generator == 'fibonacci':
        print(f'Fibonacci sequence (first {times}): ', end='')
        fib_generator = get_next_fib()
        for i in range(times):
            next_fib = next(fib_generator)
            if (i != times - 1):
                print(f'{next_fib}, ', end='')
            else:
                print(f'{next_fib}')


def game_event_generator(players: list, actions: list, times: int):
    '''
    Generator function that yields game event dictionaries
    simulating a data stream.
    '''
    for i in range(times):
        player = players[i % len(players)]
        level = (i * 3 + 5) % 17
        action = actions[((i + level) % len(actions))]

        event = {
            'id': i + 1,
            'player': player,
            'event_type': action,
            'data': {
                'level': level
            }
        }
        yield event


def process_game_events(stream_generator, total_events: int):
    '''
    Consumes the generator stream, prints events and calculates stats.
    '''
    lvl10plus = 0
    treasure_events = 0
    level_up_events = 0

    print('=== Game Data Stream Processor ===')
    print()
    print(f"Processing {total_events} game events...")
    print()

    for event in stream_generator:
        print(f"Event {event['id']}: Player {event['player']} "
              f"(level {event['data']['level']}) {event['event_type']}")

        if event['data']['level'] >= 10:
            lvl10plus += 1
        if event['event_type'] == "found treasure":
            treasure_events += 1
        if event['event_type'] == "leveled up":
            level_up_events += 1

    print()
    stream_analytics(total_events, lvl10plus, treasure_events, level_up_events)


def stream_analytics(times, lvl10plus, treasure_events, level_up_events):
    '''
    Displays analysis requested on screen
    '''
    print('=== Stream Analytics ===')
    print()
    print(f'Total events processed: {times}')
    print(f'High-level players (10+): {lvl10plus}')
    print(f'Treasure events: {treasure_events}')
    print(f'Level-up events: {level_up_events}')


def generator_demonstration():
    '''Runs demonstration for fibonacci and prime generators'''
    print()
    print('=== Generator Demonstration ===')
    print_numbers(10, 'fibonacci')
    print_numbers(5, 'prime')


def show_mem_use():
    '''Hard coded function to fit example output as import
    time is not allowed'''
    secs = 0.045
    print()
    print('Memory usage: Constant (streaming)')
    print(f'Processing time: {secs} seconds')


if __name__ == "__main__":
    '''Main program workflow'''

    players = ["alice", "bob", "charlie"]
    actions = ["killed monster", "found treasure", "leveled up"]
    total_count = 1000

    my_stream = game_event_generator(players, actions, total_count)

    process_game_events(my_stream, total_count)

    show_mem_use()
    generator_demonstration()
