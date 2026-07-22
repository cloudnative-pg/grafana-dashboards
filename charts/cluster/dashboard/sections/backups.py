"""Backups row (collapsed).

Transcribed from the original grafana-dashboard.json (panel indices 62-62), rewritten
using grafanalib's typed panel classes where they cleanly model this dashboard's
(modern) panel schema. Panel types where grafanalib only models an older/incompatible
Grafana schema are kept as plain dicts (see inline notes).
"""

from grafanalib.core import GridPos, RowPanel, TimeSeries

panels = [
    RowPanel(
        title="Backups",
        dataSource={"uid": "prometheus"},
        gridPos=GridPos(h=1, w=24, x=0, y=55),
        id=239,
        targets=[{"datasource": {"uid": "prometheus"}, "refId": "A"}],
        collapsed=True,
        panels=[
            TimeSeries(
                title="First Recoverability Point",
                dataSource={"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                gridPos=GridPos(h=6, w=8, x=0, y=56),
                id=237,
                targets=[
                    {
                        "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                        "exemplar": True,
                        "expr": '{__name__=~"cnpg_collector_first_recoverability_point|barman_cloud_cloudnative_pg_io_first_recoverability_point",namespace=~"$namespace",pod=~"$instances"}*1000 '
                        "> 0",
                        "format": "time_series",
                        "interval": "",
                        "legendFormat": "{{pod}}",
                        "refId": "A",
                    }
                ],
                extraJson={
                    "fieldConfig": {
                        "defaults": {
                            "color": {"mode": "palette-classic"},
                            "custom": {
                                "axisBorderShow": False,
                                "axisCenteredZero": False,
                                "axisColorMode": "text",
                                "axisLabel": "",
                                "axisPlacement": "auto",
                                "barAlignment": 0,
                                "drawStyle": "line",
                                "fillOpacity": 0,
                                "gradientMode": "none",
                                "hideFrom": {
                                    "legend": False,
                                    "tooltip": False,
                                    "viz": False,
                                },
                                "insertNulls": False,
                                "lineInterpolation": "linear",
                                "lineWidth": 1,
                                "pointSize": 5,
                                "scaleDistribution": {"type": "linear"},
                                "showPoints": "auto",
                                "spanNulls": False,
                                "stacking": {"group": "A", "mode": "none"},
                                "thresholdsStyle": {"mode": "off"},
                            },
                            "mappings": [],
                            "thresholds": {
                                "mode": "absolute",
                                "steps": [
                                    {"color": "green"},
                                    {"color": "red", "value": 80},
                                ],
                            },
                            "unit": "dateTimeAsIso",
                            "unitScale": True,
                        },
                        "overrides": [],
                    },
                    "options": {
                        "legend": {
                            "calcs": [],
                            "displayMode": "list",
                            "placement": "bottom",
                            "showLegend": True,
                        },
                        "tooltip": {"mode": "multi", "sort": "none"},
                    },
                },
            ),
        ],
    ),
]
