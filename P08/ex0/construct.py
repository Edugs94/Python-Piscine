import os
import site
import sys


def main() -> None:
    """Detect and display the current Python environment status."""
    try:
        real_prefix = (
            getattr(sys, "base_prefix", None)
            or getattr(sys, "real_prefix", None)
            or sys.prefix
        )
        is_venv: bool = sys.prefix != real_prefix
        current_python: str = sys.executable

        if is_venv:
            print("MATRIX STATUS: Welcome to the construct")
            print()
            print(f"Current Python: {current_python}")
            venv_name: str = os.path.basename(sys.prefix)
            print(f"Virtual Environment: {venv_name}")
            print(f"Environment Path: {sys.prefix}")
            print()
            print("SUCCESS: You're in an isolated environment!")
            print("Safe to install packages without affecting")
            print("the global system.")
            print()
            try:
                paths = site.getsitepackages()
                print(f"Package installation path: {paths[0]}")
            except (AttributeError, IndexError):
                print("Package installation path: (Standard path unavailable)")
        else:
            print("MATRIX STATUS: You're still plugged in")
            print()
            print(f"Current Python: {current_python}")
            print("Virtual Environment: None detected")
            print()
            print("WARNING: You're in the global environment!")
            print("The machines can see everything you install.")
            print()
            print("To enter the construct, run:")
            print("python -m venv matrix_env")
            print("source matrix_env/bin/activate # On Unix")
            print("matrix_env")
            print("Scripts")
            print("activate # On Windows")
            print()
            print("Then run this program again.")

    except Exception as e:
        print(f"Unexpected error: {e}")


if __name__ == "__main__":
    main()
