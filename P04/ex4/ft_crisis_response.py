def file_handler(file_name: str):
    try:
        with open(file_name, "r") as fd:
            data: str = fd.read()
            print('SUCCESS: Archive recovered '
                  f'- "{data}"')
            print('STATUS: Normal operations resumed')
    except FileNotFoundError:
        print('RESPONSE: Archive not found in storage matrix')
        print('STATUS: Crisis handled, system stable')
        return
    except PermissionError:
        print('RESPONSE: Security protocols deny access')
        print('STATUS: Crisis handled, security maintained')
        return
    finally:
        print()


def main():
    '''
    Main workflow of the program
    '''
    fd1: str = 'lost_archive.txt'
    fd2: str = 'classified_vault.txt'
    fd3: str = 'standard_archive.txt'

    print('=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===')
    print()
    print(f"CRISIS ALERT: Attempting access to '{fd1}'...")
    file_handler(fd1)
    print(f"CRISIS ALERT: Attempting access to '{fd2}'...")
    file_handler(fd2)
    print(f"ROUTINE ACCESS: Attempting access to '{fd3}'...")
    file_handler(fd3)
    print('All crisis scenarios handled successfully. Archives secure.')


if __name__ == "__main__":
    main()
