"""Regenerate ../grafana-dashboard.json from the grafanalib source in this directory.

Run with:

    uv sync && uv run main.py
"""

import os

from grafanalib._gen import loader, write_dashboard

HERE = os.path.dirname(os.path.abspath(__file__))
DASHBOARD_SOURCE = os.path.join(HERE, "cluster.dashboard.py")
OUTPUT_PATH = os.path.normpath(os.path.join(HERE, os.pardir, "grafana-dashboard.json"))


def main():
    dashboard = loader(DASHBOARD_SOURCE)
    with open(OUTPUT_PATH, "w") as output:
        write_dashboard(dashboard, output)
    print(f"Wrote {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
