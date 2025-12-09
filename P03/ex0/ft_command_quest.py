"""Exercise 0: Command Quest."""

import sys


def main():
    """Receive and print command-line arguments."""

    argc = len(sys.argv)
    print('=== Command Quest ===')

    if argc < 2:
        print('No arguments provided!')

    print(f'Program name: {sys.argv[0]}')

    i = 1
    while i < argc:
        print(f'Argument {i}: {sys.argv[i]}')
        i += 1

    print(f'Total arguments: {argc}')


if __name__ == '__main__':
    main()
