"""Checkpoints row (collapsed).

Transcribed from the original grafana-dashboard.json (panel indices 63-63), rewritten
using grafanalib's typed panel classes where they cleanly model this dashboard's
(modern) panel schema. Panel types where grafanalib only models an older/incompatible
Grafana schema are kept as plain dicts (see inline notes).
"""

from grafanalib.core import GridPos, RowPanel, TimeSeries

panels = [
    RowPanel(
        title="Checkpoints",
        dataSource={"uid": "prometheus"},
        gridPos=GridPos(h=1, w=24, x=0, y=56),
        id=293,
        targets=[{"datasource": {"uid": "prometheus"}, "refId": "A"}],
        collapsed=True,
        panels=[
            TimeSeries(
                title="Requested/Timed",
                dataSource={"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                description="",
                gridPos=GridPos(h=6, w=5, x=0, y=57),
                id=295,
                targets=[
                    {
                        "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                        "exemplar": True,
                        "expr": '{__name__=~"cnpg_pg_stat_(bgwriter|checkpointer)_checkpoints_req",namespace=~"$namespace",pod=~"$instances"}',
                        "format": "time_series",
                        "hide": False,
                        "instant": False,
                        "interval": "",
                        "intervalFactor": 1,
                        "legendFormat": "req/{{pod}}",
                        "refId": "B",
                    },
                    {
                        "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                        "exemplar": True,
                        "expr": '{__name__=~"cnpg_pg_stat_(bgwriter|checkpointer)_checkpoints_timed",namespace=~"$namespace",pod=~"$instances"}',
                        "format": "time_series",
                        "interval": "",
                        "intervalFactor": 1,
                        "legendFormat": "timed/{{pod}}",
                        "refId": "A",
                    },
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
                                "barAlignment": -1,
                                "drawStyle": "line",
                                "fillOpacity": 8,
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
                                "showPoints": "never",
                                "spanNulls": True,
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
                            "unit": "none",
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
                    "pluginVersion": "8.2.1",
                },
            ),
            TimeSeries(
                title="Write/Sync time",
                dataSource={"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                description="",
                gridPos=GridPos(h=6, w=5, x=5, y=57),
                id=296,
                targets=[
                    {
                        "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                        "exemplar": True,
                        "expr": '{__name__=~"cnpg_pg_stat_(bgwriter_checkpoint|checkpointer)_write_time",namespace=~"$namespace",pod=~"$instances"}',
                        "format": "time_series",
                        "hide": False,
                        "instant": False,
                        "interval": "",
                        "intervalFactor": 1,
                        "legendFormat": "write/{{pod}}",
                        "refId": "B",
                    },
                    {
                        "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                        "exemplar": True,
                        "expr": '{__name__=~"cnpg_pg_stat_(bgwriter_checkpoint|checkpointer)_sync_time",namespace=~"$namespace",pod=~"$instances"}',
                        "format": "time_series",
                        "interval": "",
                        "intervalFactor": 1,
                        "legendFormat": "sync/{{pod}}",
                        "refId": "A",
                    },
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
                                "barAlignment": -1,
                                "drawStyle": "line",
                                "fillOpacity": 8,
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
                                "showPoints": "never",
                                "spanNulls": True,
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
                            "unit": "ms",
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
                    "pluginVersion": "8.2.1",
                },
            ),
        ],
    ),
]
