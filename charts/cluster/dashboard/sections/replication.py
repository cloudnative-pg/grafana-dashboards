"""Replication row (collapsed).

Transcribed from the original grafana-dashboard.json (panel indices 60-60), rewritten
using grafanalib's typed panel classes where they cleanly model this dashboard's
(modern) panel schema. Panel types where grafanalib only models an older/incompatible
Grafana schema are kept as plain dicts (see inline notes).
"""

from grafanalib.core import GridPos, RowPanel, TimeSeries

panels = [
    RowPanel(
        title="Replication",
        dataSource={"uid": "prometheus"},
        gridPos=GridPos(h=1, w=24, x=0, y=53),
        id=18,
        targets=[{"datasource": {"uid": "prometheus"}, "refId": "A"}],
        collapsed=True,
        panels=[
            TimeSeries(
                title="Replication Lag",
                dataSource={"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                gridPos=GridPos(h=8, w=6, x=0, y=59),
                id=16,
                targets=[
                    {
                        "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                        "exemplar": True,
                        "expr": 'cnpg_pg_replication_lag{namespace=~"$namespace",pod=~"$instances"}',
                        "instant": False,
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
                                "fillOpacity": 10,
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
                                "thresholdsStyle": {"mode": "line"},
                            },
                            "mappings": [],
                            "thresholds": {
                                "mode": "absolute",
                                "steps": [
                                    {"color": "green"},
                                    {"color": "#EAB839", "value": 600},
                                    {"color": "dark-red", "value": 3600},
                                ],
                            },
                            "unit": "s",
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
            TimeSeries(
                title="Write Lag",
                dataSource={"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                gridPos=GridPos(h=8, w=6, x=6, y=59),
                id=14,
                targets=[
                    {
                        "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                        "editorMode": "code",
                        "exemplar": True,
                        "expr": 'cnpg_pg_stat_replication_write_lag_seconds{namespace=~"$namespace",pod=~"$instances"}',
                        "instant": False,
                        "interval": "",
                        "legendFormat": "{{pod}} -> {{application_name}}",
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
                                "fillOpacity": 10,
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
                            "unit": "s",
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
            TimeSeries(
                title="Flush Lag",
                dataSource={"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                gridPos=GridPos(h=8, w=6, x=12, y=59),
                id=59,
                targets=[
                    {
                        "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                        "editorMode": "code",
                        "exemplar": True,
                        "expr": 'cnpg_pg_stat_replication_flush_lag_seconds{namespace=~"$namespace",pod=~"$instances"}',
                        "instant": False,
                        "interval": "",
                        "legendFormat": "{{pod}} -> {{application_name}}",
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
                                "fillOpacity": 10,
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
                            "unit": "s",
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
            TimeSeries(
                title="Replay Lag",
                dataSource={"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                description="",
                gridPos=GridPos(h=8, w=6, x=18, y=59),
                id=20,
                targets=[
                    {
                        "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                        "editorMode": "code",
                        "exemplar": True,
                        "expr": 'cnpg_pg_stat_replication_replay_lag_seconds{namespace=~"$namespace",pod=~"$instances"}',
                        "interval": "",
                        "legendFormat": "{{pod}} -> {{application_name}}",
                        "range": True,
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
                                "fillOpacity": 10,
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
                            "unit": "s",
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
