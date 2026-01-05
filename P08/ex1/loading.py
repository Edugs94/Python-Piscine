import sys
from typing import Any

libraries_missing = False

try:
    import pandas as pd

    print(f"[OK] pandas ({pd.__version__}) - Data manipulation ready")
except ImportError:
    print("pandas: Not installed")
    libraries_missing = True

try:
    import requests

    print(f"[OK] requests ({requests.__version__}) - Network access ready")
except ImportError:
    print("requests: Not installed")
    libraries_missing = True

try:
    import matplotlib
    import matplotlib.pyplot as plt

    print(f"[OK] matplotlib ({matplotlib.__version__}) - Visualization ready")
except ImportError:
    print("matplotlib: Not installed")
    libraries_missing = True


def main():
    if libraries_missing is True:
        print("One or more libraries are missing. "
              "Install them with pip or Poetry")
        exit()

    try:
        response = requests.get("https://www.python.org")
        print(f"Connection established. Status Code: {response.status_code}")
    except requests.RequestException as e:
        print(f"Connection failed: {e}")
    if "pandas" in sys.modules:
        data: dict[str, Any] = {
            "Month": ["Jan", "Feb", "Mar", "Apr"],
            "Revenue": [99, 58, 83, 27],
        }

        df = pd.DataFrame(data)
        print("\nAnalyzing Matrix data...")
        print(df)

        if "matplotlib.pyplot" in sys.modules:
            print("\nGenerating visualization...")

            df.plot(kind="bar", x="Month", y="Revenue", color="blue")
            plt.title("Last months Revenue")
            plt.savefig("chart.png")
            print("Results saved to: chart.png")

        else:
            print("\nMatplotlib not installed. Skipping visualization.")

    else:
        print("\nPandas not installed. Cannot analyze data.")


if __name__ == "__main__":
    main()
