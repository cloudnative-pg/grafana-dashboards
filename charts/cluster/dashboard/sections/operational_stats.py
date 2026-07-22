"""Operational Stats row.

Transcribed from the original grafana-dashboard.json (panel indices 50-57), rewritten
using grafanalib's typed panel classes where they cleanly model this dashboard's
(modern) panel schema. Panel types where grafanalib only models an older/incompatible
Grafana schema are kept as plain dicts (see inline notes).
"""

from grafanalib.core import GridPos, RowPanel, TimeSeries

panels = [
    RowPanel(
        title="Operational Stats",
        dataSource={"uid": "prometheus"},
        gridPos=GridPos(h=1, w=24, x=0, y=19),
        id=10,
        targets=[{"datasource": {"uid": "prometheus"}, "refId": "A"}],
        collapsed=False,
        panels=[],
    ),
    TimeSeries(
        title="CPU Usage",
        dataSource={"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
        gridPos=GridPos(h=7, w=12, x=0, y=20),
        id=273,
        targets=[
            {
                "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                "exemplar": True,
                "expr": 'sum(node_namespace_pod_container:container_cpu_usage_seconds_total:sum_irate{pod=~"$instances", '
                'namespace=~"$namespace"}) by (pod)',
                "format": "time_series",
                "interval": "",
                "intervalFactor": 2,
                "legendFormat": "{{pod}}",
                "refId": "A",
                "step": 10,
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
                        "fillOpacity": 100,
                        "gradientMode": "none",
                        "hideFrom": {"legend": False, "tooltip": False, "viz": False},
                        "insertNulls": False,
                        "lineInterpolation": "linear",
                        "lineWidth": 2,
                        "pointSize": 5,
                        "scaleDistribution": {"log": 10, "type": "log"},
                        "showPoints": "never",
                        "spanNulls": False,
                        "stacking": {"group": "A", "mode": "normal"},
                        "thresholdsStyle": {"mode": "off"},
                    },
                    "mappings": [],
                    "min": 0,
                    "thresholds": {
                        "mode": "absolute",
                        "steps": [
                            {"color": "green", "value": None},
                            {"color": "red", "value": 80},
                        ],
                    },
                    "unit": "short",
                    "unitScale": True,
                },
                "overrides": [],
            },
            "links": [],
            "options": {
                "legend": {
                    "calcs": [],
                    "displayMode": "list",
                    "placement": "bottom",
                    "showLegend": True,
                },
                "tooltip": {"mode": "multi", "sort": "desc"},
            },
            "pluginVersion": "10.3.1",
        },
    ),
    TimeSeries(
        title="Memory Usage (container memory working set)",
        dataSource={"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
        gridPos=GridPos(h=7, w=12, x=12, y=20),
        id=275,
        targets=[
            {
                "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                "exemplar": True,
                "expr": 'sum(container_memory_working_set_bytes{pod=~"$instances", '
                'namespace="$namespace", container!="", image!=""}) by (pod)',
                "format": "time_series",
                "interval": "",
                "intervalFactor": 2,
                "legendFormat": "{{pod}}",
                "refId": "A",
                "step": 10,
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
                        "fillOpacity": 100,
                        "gradientMode": "none",
                        "hideFrom": {"legend": False, "tooltip": False, "viz": False},
                        "insertNulls": False,
                        "lineInterpolation": "linear",
                        "lineWidth": 2,
                        "pointSize": 5,
                        "scaleDistribution": {"type": "linear"},
                        "showPoints": "never",
                        "spanNulls": False,
                        "stacking": {"group": "A", "mode": "none"},
                        "thresholdsStyle": {"mode": "off"},
                    },
                    "mappings": [],
                    "min": 0,
                    "thresholds": {
                        "mode": "absolute",
                        "steps": [
                            {"color": "green", "value": None},
                            {"color": "red", "value": 80},
                        ],
                    },
                    "unit": "bytes",
                    "unitScale": True,
                },
                "overrides": [
                    {
                        "matcher": {"id": "byName", "options": "quota - requests"},
                        "properties": [
                            {
                                "id": "color",
                                "value": {"fixedColor": "#F2495C", "mode": "fixed"},
                            },
                            {"id": "custom.fillOpacity", "value": 0},
                            {"id": "custom.lineWidth", "value": 2},
                            {
                                "id": "custom.stacking",
                                "value": {"group": "A", "mode": "none"},
                            },
                            {
                                "id": "custom.lineStyle",
                                "value": {"dash": [10, 10], "fill": "dash"},
                            },
                        ],
                    },
                    {
                        "matcher": {"id": "byName", "options": "quota - limits"},
                        "properties": [
                            {
                                "id": "color",
                                "value": {"fixedColor": "#FF9830", "mode": "fixed"},
                            },
                            {"id": "custom.fillOpacity", "value": 0},
                            {"id": "custom.lineWidth", "value": 2},
                            {
                                "id": "custom.stacking",
                                "value": {"group": "A", "mode": "none"},
                            },
                            {
                                "id": "custom.lineStyle",
                                "value": {"dash": [10, 10], "fill": "dash"},
                            },
                        ],
                    },
                ],
            },
            "links": [],
            "options": {
                "legend": {
                    "calcs": [],
                    "displayMode": "list",
                    "placement": "bottom",
                    "showLegend": True,
                },
                "tooltip": {"mode": "multi", "sort": "desc"},
            },
            "pluginVersion": "10.3.1",
        },
    ),
    TimeSeries(
        title="Session States",
        dataSource={"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
        description="",
        gridPos=GridPos(h=8, w=24, x=0, y=27),
        id=39,
        targets=[
            {
                "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                "exemplar": True,
                "expr": 'sum(cnpg_backends_total{namespace=~"$namespace",pod=~"$instances"}) by '
                "(pod)",
                "hide": False,
                "interval": "",
                "legendFormat": "total ({{pod}})",
                "refId": "B",
            },
            {
                "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                "exemplar": True,
                "expr": 'sum(cnpg_backends_total{namespace=~"$namespace",pod=~"$instances"}) by '
                "(state, pod)",
                "interval": "",
                "legendFormat": "{{state}} ({{pod}})",
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
                        "barAlignment": 0,
                        "drawStyle": "line",
                        "fillOpacity": 10,
                        "gradientMode": "opacity",
                        "hideFrom": {"legend": False, "tooltip": False, "viz": False},
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
                        "steps": [{"color": "green", "value": None}],
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
        title="Transactions [5m]",
        dataSource={"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
        gridPos=GridPos(h=8, w=12, x=0, y=35),
        id=50,
        targets=[
            {
                "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                "editorMode": "code",
                "exemplar": True,
                "expr": 'sum(rate(cnpg_pg_stat_database_xact_commit{namespace=~"$namespace",pod=~"$instances"}[5m])) '
                "by (pod)",
                "interval": "",
                "legendFormat": "committed ({{pod}})",
                "range": True,
                "refId": "A",
            },
            {
                "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                "exemplar": True,
                "expr": 'sum(rate(cnpg_pg_stat_database_xact_rollback{namespace=~"$namespace",pod=~"$instances"}[5m])) '
                "by (pod)",
                "hide": False,
                "interval": "",
                "legendFormat": "rolled back ({{pod}})",
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
                        "gradientMode": "opacity",
                        "hideFrom": {"legend": False, "tooltip": False, "viz": False},
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
                        "steps": [{"color": "green"}, {"color": "red", "value": 80}],
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
        title="Longest Transaction",
        dataSource={"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
        description="",
        gridPos=GridPos(h=8, w=12, x=12, y=35),
        id=4,
        targets=[
            {
                "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                "exemplar": True,
                "expr": "max by (pod) "
                '(cnpg_backends_max_tx_duration_seconds{namespace=~"$namespace",pod=~"$instances"})',
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
                        "hideFrom": {"legend": False, "tooltip": False, "viz": False},
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
                        "steps": [{"color": "green"}, {"color": "red", "value": 80}],
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
        title="Deadlocks [5m]",
        dataSource={"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
        description="",
        gridPos=GridPos(h=8, w=12, x=0, y=43),
        id=55,
        targets=[
            {
                "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                "exemplar": True,
                "expr": 'rate(cnpg_pg_stat_database_deadlocks{datname="",namespace=~"$namespace",pod=~"$instances"}[5m])',
                "hide": False,
                "instant": False,
                "interval": "",
                "legendFormat": "count ({{pod}})",
                "refId": "B",
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
                        "hideFrom": {"legend": False, "tooltip": False, "viz": False},
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
                        "steps": [{"color": "green"}, {"color": "red", "value": 80}],
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
        title="Blocked Queries",
        dataSource={"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
        description="",
        gridPos=GridPos(h=8, w=12, x=12, y=43),
        id=54,
        targets=[
            {
                "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                "exemplar": True,
                "expr": 'cnpg_backends_waiting_total{namespace=~"$namespace",pod=~"$instances"}',
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
                        "hideFrom": {"legend": False, "tooltip": False, "viz": False},
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
                        "steps": [{"color": "green"}, {"color": "red", "value": 80}],
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
]
