"""Write Ahead Log row (collapsed).

Transcribed from the original grafana-dashboard.json (panel indices 59-59), rewritten
using grafanalib's typed panel classes where they cleanly model this dashboard's
(modern) panel schema. Panel types where grafanalib only models an older/incompatible
Grafana schema are kept as plain dicts (see inline notes).
"""

from grafanalib.core import GridPos, RowPanel, TimeSeries

panels = [
    RowPanel(
        title="Write Ahead Log",
        dataSource={"uid": "prometheus"},
        gridPos=GridPos(h=1, w=24, x=0, y=52),
        id=37,
        targets=[{"datasource": {"uid": "prometheus"}, "refId": "A"}],
        collapsed=True,
        panels=[
            TimeSeries(
                title="WAL Segment Archive Status",
                dataSource={"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                gridPos=GridPos(h=8, w=8, x=0, y=53),
                id=6,
                targets=[
                    {
                        "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                        "exemplar": True,
                        "expr": 'cnpg_collector_pg_wal_archive_status{value="ready",namespace=~"$namespace",pod=~"$instances"}',
                        "interval": "",
                        "legendFormat": "ready ({{pod}})",
                        "refId": "A",
                    },
                    {
                        "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                        "exemplar": True,
                        "expr": 'cnpg_collector_pg_wal_archive_status{value="done",namespace=~"$namespace",pod=~"$instances"}',
                        "hide": False,
                        "interval": "",
                        "legendFormat": "done ({{pod}})",
                        "refId": "B",
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
                title="Archiver Status [5m]",
                dataSource={"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                gridPos=GridPos(h=8, w=8, x=8, y=53),
                id=52,
                targets=[
                    {
                        "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                        "exemplar": True,
                        "expr": 'rate(cnpg_pg_stat_archiver_archived_count{namespace=~"$namespace",pod=~"$instances"}[5m])',
                        "interval": "",
                        "legendFormat": "archived ({{pod}})",
                        "refId": "A",
                    },
                    {
                        "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                        "exemplar": True,
                        "expr": 'rate(cnpg_pg_stat_archiver_failed_count{namespace=~"$namespace",pod=~"$instances"}[5m])',
                        "hide": False,
                        "interval": "",
                        "legendFormat": "failed ({{pod}})",
                        "refId": "B",
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
                title="Last Archive Age",
                dataSource={"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                description="",
                gridPos=GridPos(h=8, w=8, x=16, y=53),
                id=53,
                targets=[
                    {
                        "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                        "exemplar": True,
                        "expr": 'cnpg_pg_stat_archiver_seconds_since_last_archival{namespace=~"$namespace",pod=~"$instances"}',
                        "interval": "",
                        "legendFormat": "age ({{pod}})",
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
                title="WAL Count",
                dataSource={"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                gridPos=GridPos(h=8, w=8, x=0, y=61),
                id=725,
                targets=[
                    {
                        "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                        "editorMode": "code",
                        "expr": 'cnpg_collector_pg_wal{pod=~"$instances", namespace=~"$namespace", '
                        'value="count"}',
                        "instant": False,
                        "legendFormat": "{{pod}}",
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
                        "tooltip": {"mode": "single", "sort": "none"},
                    },
                },
            ),
        ],
    ),
]
