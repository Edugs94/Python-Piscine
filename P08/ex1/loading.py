import sys
from typing import Any

try:
    import pandas as pd

    print("pandas: OK")
except ImportError:
    print("pandas: Not installed")

try:
    import requests

    print("requests: OK")
except ImportError:
    print("requests: Not installed")

try:
    import matplotlib.pyplot as plt

    print("matplotlib: OK")
except ImportError:
    print("matplotlib: Not installed")


def main():
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
