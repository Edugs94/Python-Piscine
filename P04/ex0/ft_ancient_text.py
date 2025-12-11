def read_and_print(fd):
    '''
    Reads fd and prints it line by line
    '''
    print('Connection established...')
    print()
    print('RECOVERED DATA:')
    data = fd.read()
    print(data)
    print()
    print('Data recovery complete. Storage unit disconnected.')


def main():
    '''
    Main workflow of the program
    '''
    file_name = "ancient_fragment.txt"
    print('=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===')
    print()
    print(f'Accessing Storage Vault: {file_name}')
    try:
        fd = open(file_name, "r")

    except FileNotFoundError:
        print('ERROR: Storage vault not found. Run data generator first.')
        return

    read_and_print(fd)
    fd.close()


if __name__ == "__main__":
    main()
