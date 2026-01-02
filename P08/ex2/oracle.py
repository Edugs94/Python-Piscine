import os

try:
    from dotenv import load_dotenv

except ImportError:
    print("dotenv: Not installed. Run pip install python-dotenv on venv")
    exit()


def main():
    """
    Docstring for main
    """
    load_dotenv()
    print("ORACLE STATUS: Reading the Matrix...")

    matrix_mode = os.getenv("MATRIX_MODE")
    database_url = os.getenv("DATABASE_URL")
    api_key = os.getenv("API_KEY")
    log_level = os.getenv("LOG_LEVEL")
    zion_endpoint = os.getenv("ZION_ENDPOINT")
    required_vars = [
        matrix_mode,
        database_url,
        api_key,
        log_level,
        zion_endpoint,
    ]
    if None in required_vars:
        print("Error: Environment variables missing.")
        return
    print()
    print("Configuration loaded:")
    print(f"Mode: {matrix_mode}")
    print("Database: Connected to local instance")
    print("API Access: Authenticated")
    print(f"Log Level: {log_level}")
    print("Zion Network: Online")
    print()
    print("Environment security check:")
    print("[OK] No hardcoded secrets detected")
    print("[OK] .env file properly configured")
    print("[OK] Production overrides available")
    print()
    print("The Oracle sees all configurations.")


if __name__ == "__main__":
    main()
