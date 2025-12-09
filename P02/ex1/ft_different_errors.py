def garden_operations(error):
    """Simulates specific Python errors based on the input error type."""

    if (error == "ValueError"):

        print(int('abc'))

    elif (error == "ZeroDivisionError"):

        print(42/0)

    elif (error == "FileNotFoundError"):
        open("no_existing_file.txt", "r")

    elif (error == "KeyError"):
        plants = {"Example_key": "Example_Value"}
        print(plants["Banana"])


def test_error_types():
    """Tests the generation and safe handling of multiple error types."""

    print('=== Garden Error Types Demo ===')
    print()

    print('Testing temperature: ValueError...')
    try:
        garden_operations("ValueError")
    except ValueError:
        print("Caught ValueError: invalid literal for int()")
    print()
    print('Testing temperature: ZeroDivisionError...')
    try:
        garden_operations("ZeroDivisionError")
    except ZeroDivisionError:
        print("Caught ZeroDivisionError: division by zero")
    print()

    print('Testing temperature: FileNotFoundError...')
    try:
        garden_operations("FileNotFoundError")
    except FileNotFoundError:
        print("Caught FileNotFoundError: No such file 'missing.txt'")
    print()

    print('Testing temperature: KeyError...')
    try:
        garden_operations("KeyError")
    except KeyError:
        print("Caught KeyError: 'missing\\_plant'")
    print()
    print('Testing multiple errors together..')
    try:
        garden_operations("ValueError")
    except (ValueError, ZeroDivisionError, FileNotFoundError, KeyError):
        print("Caught an error, but program continues!")
    print()
    print("All error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
