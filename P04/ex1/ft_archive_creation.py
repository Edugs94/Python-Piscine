def write_and_print(fd, data):
    """
    Overwrite data on file
    """
    print("Storage unit created successfully..")
    print()
    print("Inscribing preservation data...")
    fd.write(data)
    print(data)
    print()
    print("Data inscription complete. Storage unit sealed.")


def main():
    """
    Open/create a file and overwrite
    """
    file_name = "new_discovery.txt"
    data = (
        "[ENTRY 001] New quantum algorithm discovered\n[ENTRY 002]"
        " Efficiency increased by 347%\n[ENTRY 003]"
        " Archived by Data Archivist trainee"
    )
    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===")
    print()
    print(f"Initializing new storage unit: {file_name}")

    fd = open(file_name, "w")

    write_and_print(fd, data)

    print(f"Archive '{file_name}' ready for long-term preservation.")
    fd.close()


if __name__ == "__main__":
    main()
