import math


def distance_caculator(x2: int, y2: int, z2: int) -> float:
    x1 = 0
    y1 = 0
    z1 = 0
    distance = math.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)
    return float(distance)


def detail_error(error: str, error_message):
    print(f"Error details - Type: {error}, Args: (\"{error_message}\",)")


def parse_coordinates(data) -> tuple:
    i = 0
    flag = 0

    try:
        parts = data.split(',')
        flag = 1
        print(f'Parsing coordinates: "{data}"')
    except AttributeError:
        print(f'Position created: {data}')
        parts = data

    for part in parts:
        try:
            int(part)
        except ValueError:
            error_message = f"invalid literal for int() with base 10: '{part}'"
            print(f"Error parsing coordinates: {error_message}")
            detail_error("ValueError", error_message)
            return
        i += 1
    if i != 3:
        print("Error: 3 coordinates are required")
        return
    x = int(parts[0])
    y = int(parts[1])
    z = int(parts[2])
    coordinates = (x, y, z)
    distance = distance_caculator(x, y, z)
    if flag == 1:
        print(f'Parsed position: {coordinates}')
    print(f'Distance between (0, 0, 0) and {coordinates}: {distance:.2f}')

    return coordinates


def main() -> None:

    print('=== Game Coordinate System ===')
    test_1 = (10, 20, 5)
    test_2 = "3,4,0"
    test_3 = "abc, def, ghi"
    parse_coordinates(test_1)
    print()
    coordinates = parse_coordinates(test_2)
    print()
    parse_coordinates(test_3)
    print()
    print('Unpacking demonstration:')
    print(f'Player at x={coordinates[0]}, y={coordinates[1]},'
          f' z={coordinates[2]}')
    x, y, z = coordinates
    print(f'Coordinates: X={x}, Y={y}, Z={z}')


if __name__ == "__main__":
    main()
