import sys


def main():
    '''
    Main worflow of the program to show info on requested channels
    '''
    print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===")
    print()
    id = input("Input Stream active. Enter archivist ID: ")
    status = input("Input Stream active. Enter status report: ")

    print()
    print("[STANDARD] Archive status from "
          f"{id}: {status}", file=sys.stdout)
    print("[ALERT] System diagnostic: Communication"
          " channels verified", file=sys.stderr)
    print("[STANDARD] Data transmission complete", file=sys.stdout)
    print()
    print('Three-channel communication test successful.')


if __name__ == "__main__":
    main()
