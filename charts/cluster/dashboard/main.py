"""Regenerate ../grafana-dashboard.json from the grafanalib source in this directory.

Run with:

    uv sync && uv run main.py
"""

import json
import os

from grafanalib._gen import DashboardEncoder

from dashboard import dashboard

HERE = os.path.dirname(os.path.abspath(__file__))
OUTPUT_PATH = os.path.normpath(os.path.join(HERE, os.pardir, "grafana-dashboard.json"))


def main():
    json_data = json.dumps(
        dashboard.to_json_data(), sort_keys=True, indent=2, cls=DashboardEncoder
    )
    with open(OUTPUT_PATH, "w") as output:
        output.write(json_data)
        output.write("\n")
    print(f"Wrote {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
