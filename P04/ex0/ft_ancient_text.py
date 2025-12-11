def read_and_print(fd):
    '''
    Reads fd and prints it line by line
    '''

    print('Connection established...')
    print('RECOVERED DATA:')
    data = fd.read()
    print(data)
    print('Data recovery complete. Storage unit disconnected')

def main():
    '''
    Main workflow of the program
    '''
    file_name = 'ancient_fragment.txt'
    print('=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===')
    print(f'Accessing Storage Vault: {file_name}')
    fd = open(file_name, "r")
    if (fd < 0):
        print('ERROR: Storage vault not found. Run data generator first.')
        return
    else:
        read_and_print(fd)
        fd.close()

if __name__ == "__main__":
    main()





'''
Accessing Storage Vault: ancient\_fragment.txt
Connection established...
RECOVERED DATA:
{[}FRAGMENT 001{]} Digital preservation protocols established 2087
{[}FRAGMENT 002{]} Knowledge must survive the entropy wars
{[}FRAGMENT 003{]} Every byte saved is a victory against oblivion

'''