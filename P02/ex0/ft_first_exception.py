def check_temperature(temp_str):
    """Validates if the temperature is a number
    within the safe range (0-40)."""

    try:
        temp = int(temp_str)

    except: # noqa
        print(f"Error: '{temp_str}' is not a valid number")
        return None

    if temp > 40:
        print(f"Error: {temp_str}°C is too hot for plants (max 40°C)")

    elif temp < 0:
        print(f"Error: {temp_str}°C is too cold for plants (min 0°C)")

    else:
        print(f"Temperature {temp_str}°C is perfect for plants!")

    return temp


def test_temperature_input():
    """Tests the temperature checker with
    valid, invalid, and boundary values."""

    print('=== Garden Temperature Checker ===')
    print()
    print('Testing temperature: 25')
    check_temperature('25')
    print()
    print('Testing temperature: abc')
    check_temperature('abc')
    print()
    print('Testing temperature: 100')
    check_temperature('100')
    print()
    print('Testing temperature: -50')
    check_temperature('-50')
    print()
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature_input()
