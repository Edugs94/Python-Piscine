def main():
    '''
    Main workflow of the program
    '''
    r_fd = "classified_data.txt"
    w_fd = "security_protocols.txt"
    print('=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===')
    print()
    print('Initiating secure vault access...')
    try:
        with open(r_fd, "r") as fd:
            print('Vault connection established with failsafe protocols')
            print()
            print('SECURE EXTRACTION:')
            data = fd.read()
            print(data)
    except FileNotFoundError:
        print
        print('ERROR: Storage vault not found. Run data generator first.')
        return
    with open(w_fd, "w") as fd:
        print()
        print('SECURE PRESERVATION:')
        preservate = '[CLASSIFIED] New security protocols archived'
        fd.write(preservate)
        print(preservate)
    print('Vault automatically sealed upon completion')
    print()
    print('All vault operations completed with maximum security.')


if __name__ == "__main__":
    main()
