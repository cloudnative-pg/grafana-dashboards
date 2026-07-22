"""Operator row (collapsed).

Transcribed from the original grafana-dashboard.json (panel indices 65-65), rewritten
using grafanalib's typed panel classes where they cleanly model this dashboard's
(modern) panel schema. Panel types where grafanalib only models an older/incompatible
Grafana schema are kept as plain dicts (see inline notes).
"""

from grafanalib.core import GridPos, RowPanel, Stat, TimeSeries

panels = [
    RowPanel(
        title="Operator",
        gridPos=GridPos(h=1, w=24, x=0, y=58),
        id=696,
        collapsed=True,
        panels=[
            Stat(
                dataSource={"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                description="",
                gridPos=GridPos(h=2, w=4, x=0, y=64),
                id=697,
                targets=[
                    {
                        "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                        "editorMode": "code",
                        "exemplar": False,
                        "expr": 'sum(kube_pod_status_ready{namespace="$operatorNamespace", '
                        'pod=~"cloudnative-pg.+|cnpg-controller-manager.+", condition="true"})',
                        "hide": False,
                        "instant": True,
                        "legendFormat": "Ready Operator Pods",
                        "range": False,
                        "refId": "A",
                    }
                ],
                extraJson={
                    "fieldConfig": {
                        "defaults": {
                            "color": {"mode": "thresholds"},
                            "mappings": [
                                {
                                    "options": {
                                        "0": {
                                            "color": "red",
                                            "index": 0,
                                            "text": "No Ready pods",
                                        }
                                    },
                                    "type": "value",
                                }
                            ],
                            "thresholds": {
                                "mode": "absolute",
                                "steps": [{"color": "green"}],
                            },
                            "unitScale": True,
                        },
                        "overrides": [
                            {
                                "matcher": {"id": "byName", "options": "A"},
                                "properties": [
                                    {"id": "displayName", "value": "Reconcile errors"}
                                ],
                            }
                        ],
                    },
                    "options": {
                        "colorMode": "background",
                        "graphMode": "none",
                        "justifyMode": "auto",
                        "orientation": "auto",
                        "reduceOptions": {
                            "calcs": ["lastNotNull"],
                            "fields": "",
                            "values": False,
                        },
                        "showPercentChange": False,
                        "textMode": "value_and_name",
                        "wideLayout": True,
                    },
                    "pluginVersion": "10.3.3",
                },
            ),
            Stat(
                dataSource={"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                description="The operator reconcile errors don't distinguish between database cluster or namespaces.",
                gridPos=GridPos(h=2, w=4, x=4, y=64),
                id=702,
                targets=[
                    {
                        "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                        "editorMode": "code",
                        "exemplar": False,
                        "expr": 'max(controller_runtime_reconcile_total{namespace=~"$operatorNamespace", '
                        'result="error", controller="cluster"})',
                        "hide": False,
                        "instant": True,
                        "legendFormat": "Cluster Reconcile Errors",
                        "range": False,
                        "refId": "RECONCILE_ERRORS_BACKUP",
                    }
                ],
                extraJson={
                    "fieldConfig": {
                        "defaults": {
                            "color": {"mode": "thresholds"},
                            "mappings": [
                                {
                                    "options": {
                                        "0": {
                                            "color": "green",
                                            "index": 0,
                                            "text": "None",
                                        }
                                    },
                                    "type": "value",
                                },
                                {
                                    "options": {
                                        "from": 1,
                                        "result": {"color": "red", "index": 1},
                                        "to": 4294967295,
                                    },
                                    "type": "range",
                                },
                            ],
                            "thresholds": {
                                "mode": "absolute",
                                "steps": [{"color": "green"}],
                            },
                            "unitScale": True,
                        },
                        "overrides": [
                            {
                                "matcher": {"id": "byName", "options": "A"},
                                "properties": [
                                    {"id": "displayName", "value": "Reconcile errors"}
                                ],
                            }
                        ],
                    },
                    "options": {
                        "colorMode": "background",
                        "graphMode": "none",
                        "justifyMode": "auto",
                        "orientation": "auto",
                        "reduceOptions": {
                            "calcs": ["lastNotNull"],
                            "fields": "",
                            "values": False,
                        },
                        "showPercentChange": False,
                        "textMode": "value_and_name",
                        "wideLayout": True,
                    },
                    "pluginVersion": "10.3.3",
                },
            ),
            Stat(
                dataSource={"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                description="The operator reconcile errors don't distinguish between database cluster or namespaces.",
                gridPos=GridPos(h=2, w=4, x=8, y=64),
                id=698,
                targets=[
                    {
                        "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                        "editorMode": "code",
                        "exemplar": False,
                        "expr": 'max(controller_runtime_reconcile_total{namespace=~"$operatorNamespace", '
                        'result="error", controller="backup"})',
                        "hide": False,
                        "instant": True,
                        "legendFormat": "Backup Reconcile Errors",
                        "range": False,
                        "refId": "RECONCILE_ERRORS_BACKUP",
                    }
                ],
                extraJson={
                    "fieldConfig": {
                        "defaults": {
                            "color": {"mode": "thresholds"},
                            "mappings": [
                                {
                                    "options": {
                                        "0": {
                                            "color": "green",
                                            "index": 0,
                                            "text": "None",
                                        }
                                    },
                                    "type": "value",
                                },
                                {
                                    "options": {
                                        "from": 1,
                                        "result": {"color": "red", "index": 1},
                                        "to": 4294967295,
                                    },
                                    "type": "range",
                                },
                            ],
                            "thresholds": {
                                "mode": "absolute",
                                "steps": [{"color": "green"}],
                            },
                            "unitScale": True,
                        },
                        "overrides": [
                            {
                                "matcher": {"id": "byName", "options": "A"},
                                "properties": [
                                    {"id": "displayName", "value": "Reconcile errors"}
                                ],
                            }
                        ],
                    },
                    "options": {
                        "colorMode": "background",
                        "graphMode": "none",
                        "justifyMode": "auto",
                        "orientation": "auto",
                        "reduceOptions": {
                            "calcs": ["lastNotNull"],
                            "fields": "",
                            "values": False,
                        },
                        "showPercentChange": False,
                        "textMode": "value_and_name",
                        "wideLayout": True,
                    },
                    "pluginVersion": "10.3.3",
                },
            ),
            Stat(
                dataSource={"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                description="The operator reconcile errors don't distinguish between database cluster or namespaces.",
                gridPos=GridPos(h=2, w=4, x=12, y=64),
                id=704,
                targets=[
                    {
                        "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                        "editorMode": "code",
                        "exemplar": False,
                        "expr": 'max(controller_runtime_reconcile_total{namespace=~"$operatorNamespace", '
                        'result="error", controller=~"scheduledbackup|scheduled-backup"})',
                        "hide": False,
                        "instant": True,
                        "legendFormat": "Scheduled Backup Reconcile Errors",
                        "range": False,
                        "refId": "RECONCILE_ERRORS_BACKUP",
                    }
                ],
                extraJson={
                    "fieldConfig": {
                        "defaults": {
                            "color": {"mode": "thresholds"},
                            "mappings": [
                                {
                                    "options": {
                                        "0": {
                                            "color": "green",
                                            "index": 0,
                                            "text": "None",
                                        }
                                    },
                                    "type": "value",
                                },
                                {
                                    "options": {
                                        "from": 1,
                                        "result": {"color": "red", "index": 1},
                                        "to": 4294967295,
                                    },
                                    "type": "range",
                                },
                            ],
                            "thresholds": {
                                "mode": "absolute",
                                "steps": [{"color": "green"}],
                            },
                            "unitScale": True,
                        },
                        "overrides": [
                            {
                                "matcher": {"id": "byName", "options": "A"},
                                "properties": [
                                    {"id": "displayName", "value": "Reconcile errors"}
                                ],
                            }
                        ],
                    },
                    "options": {
                        "colorMode": "background",
                        "graphMode": "none",
                        "justifyMode": "auto",
                        "orientation": "auto",
                        "reduceOptions": {
                            "calcs": ["lastNotNull"],
                            "fields": "",
                            "values": False,
                        },
                        "showPercentChange": False,
                        "textMode": "value_and_name",
                        "wideLayout": True,
                    },
                    "pluginVersion": "10.3.3",
                },
            ),
            Stat(
                dataSource={"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                description="The operator reconcile errors don't distinguish between database cluster or namespaces.",
                gridPos=GridPos(h=2, w=4, x=16, y=64),
                id=703,
                targets=[
                    {
                        "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                        "editorMode": "code",
                        "exemplar": False,
                        "expr": 'max(controller_runtime_reconcile_total{namespace=~"$operatorNamespace", '
                        'result="error", controller="pooler"})',
                        "hide": False,
                        "instant": True,
                        "legendFormat": "Pooler Reconcile Errors",
                        "range": False,
                        "refId": "RECONCILE_ERRORS_BACKUP",
                    }
                ],
                extraJson={
                    "fieldConfig": {
                        "defaults": {
                            "color": {"mode": "thresholds"},
                            "mappings": [
                                {
                                    "options": {
                                        "0": {
                                            "color": "green",
                                            "index": 0,
                                            "text": "None",
                                        }
                                    },
                                    "type": "value",
                                },
                                {
                                    "options": {
                                        "from": 1,
                                        "result": {"color": "red", "index": 1},
                                        "to": 4294967295,
                                    },
                                    "type": "range",
                                },
                            ],
                            "thresholds": {
                                "mode": "absolute",
                                "steps": [{"color": "green"}],
                            },
                            "unitScale": True,
                        },
                        "overrides": [
                            {
                                "matcher": {"id": "byName", "options": "A"},
                                "properties": [
                                    {"id": "displayName", "value": "Reconcile errors"}
                                ],
                            }
                        ],
                    },
                    "options": {
                        "colorMode": "background",
                        "graphMode": "none",
                        "justifyMode": "auto",
                        "orientation": "auto",
                        "reduceOptions": {
                            "calcs": ["lastNotNull"],
                            "fields": "",
                            "values": False,
                        },
                        "showPercentChange": False,
                        "textMode": "value_and_name",
                        "wideLayout": True,
                    },
                    "pluginVersion": "10.3.3",
                },
            ),
            TimeSeries(
                title="Ready Operator Pods",
                dataSource={"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                description="",
                gridPos=GridPos(h=8, w=4, x=0, y=66),
                id=746,
                targets=[
                    {
                        "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                        "editorMode": "code",
                        "expr": 'sum(kube_pod_status_ready{namespace="$operatorNamespace", '
                        'pod=~"cloudnative-pg.+|cnpg-controller-manager.+", condition="true"})',
                        "hide": False,
                        "instant": False,
                        "legendFormat": "Ready Operator Pods",
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
                            "mappings": [
                                {
                                    "options": {
                                        "0": {
                                            "color": "red",
                                            "index": 0,
                                            "text": "No Ready pods",
                                        }
                                    },
                                    "type": "value",
                                }
                            ],
                            "thresholds": {
                                "mode": "absolute",
                                "steps": [{"color": "green"}],
                            },
                            "unitScale": True,
                        },
                        "overrides": [
                            {
                                "matcher": {"id": "byName", "options": "A"},
                                "properties": [
                                    {"id": "displayName", "value": "Reconcile errors"}
                                ],
                            }
                        ],
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
                    "pluginVersion": "10.3.3",
                },
            ),
            TimeSeries(
                title="Cluster Reconcile Errors",
                dataSource={"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                description="The operator reconcile errors don't distinguish between database cluster or namespaces.",
                gridPos=GridPos(h=8, w=4, x=4, y=66),
                id=767,
                targets=[
                    {
                        "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                        "editorMode": "code",
                        "expr": 'max(controller_runtime_reconcile_total{namespace=~"$operatorNamespace", '
                        'result="error", controller="cluster"})',
                        "hide": False,
                        "legendFormat": "Cluster Reconcile Errors",
                        "range": True,
                        "refId": "RECONCILE_ERRORS_BACKUP",
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
                            "mappings": [
                                {
                                    "options": {
                                        "0": {
                                            "color": "green",
                                            "index": 0,
                                            "text": "None",
                                        }
                                    },
                                    "type": "value",
                                },
                                {
                                    "options": {
                                        "from": 1,
                                        "result": {"color": "red", "index": 1},
                                        "to": 4294967295,
                                    },
                                    "type": "range",
                                },
                            ],
                            "thresholds": {
                                "mode": "absolute",
                                "steps": [{"color": "green"}],
                            },
                            "unitScale": True,
                        },
                        "overrides": [
                            {
                                "matcher": {"id": "byName", "options": "A"},
                                "properties": [
                                    {"id": "displayName", "value": "Reconcile errors"}
                                ],
                            }
                        ],
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
                    "pluginVersion": "10.3.3",
                },
            ),
            TimeSeries(
                title="Backup Reconcile Errors",
                dataSource={"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                description="The operator reconcile errors don't distinguish between database cluster or namespaces.",
                gridPos=GridPos(h=8, w=4, x=8, y=66),
                id=768,
                targets=[
                    {
                        "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                        "editorMode": "code",
                        "expr": 'max(controller_runtime_reconcile_total{namespace=~"$operatorNamespace", '
                        'result="error", controller="backup"})',
                        "hide": False,
                        "legendFormat": "Backup Reconcile Errors",
                        "range": True,
                        "refId": "RECONCILE_ERRORS_BACKUP",
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
                            "mappings": [
                                {
                                    "options": {
                                        "0": {
                                            "color": "green",
                                            "index": 0,
                                            "text": "None",
                                        }
                                    },
                                    "type": "value",
                                },
                                {
                                    "options": {
                                        "from": 1,
                                        "result": {"color": "red", "index": 1},
                                        "to": 4294967295,
                                    },
                                    "type": "range",
                                },
                            ],
                            "thresholds": {
                                "mode": "absolute",
                                "steps": [{"color": "green"}],
                            },
                            "unitScale": True,
                        },
                        "overrides": [
                            {
                                "matcher": {"id": "byName", "options": "A"},
                                "properties": [
                                    {"id": "displayName", "value": "Reconcile errors"}
                                ],
                            }
                        ],
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
                    "pluginVersion": "10.3.3",
                },
            ),
            TimeSeries(
                title="Scheduled Backup Reconcile Errors",
                dataSource={"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                description="The operator reconcile errors don't distinguish between database cluster or namespaces.",
                gridPos=GridPos(h=8, w=4, x=12, y=66),
                id=790,
                targets=[
                    {
                        "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                        "editorMode": "code",
                        "exemplar": False,
                        "expr": 'max(controller_runtime_reconcile_total{namespace=~"$operatorNamespace", '
                        'result="error", controller=~"scheduledbackup|scheduled-backup"})',
                        "hide": False,
                        "instant": False,
                        "legendFormat": "Scheduled Backup Reconcile Errors",
                        "range": True,
                        "refId": "RECONCILE_ERRORS_BACKUP",
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
                            "mappings": [
                                {
                                    "options": {
                                        "0": {
                                            "color": "green",
                                            "index": 0,
                                            "text": "None",
                                        }
                                    },
                                    "type": "value",
                                },
                                {
                                    "options": {
                                        "from": 1,
                                        "result": {"color": "red", "index": 1},
                                        "to": 4294967295,
                                    },
                                    "type": "range",
                                },
                            ],
                            "thresholds": {
                                "mode": "absolute",
                                "steps": [{"color": "green"}],
                            },
                            "unitScale": True,
                        },
                        "overrides": [
                            {
                                "matcher": {"id": "byName", "options": "A"},
                                "properties": [
                                    {"id": "displayName", "value": "Reconcile errors"}
                                ],
                            }
                        ],
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
                    "pluginVersion": "10.3.3",
                },
            ),
            TimeSeries(
                title="Pooler Reconcile Errors",
                dataSource={"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                description="The operator reconcile errors don't distinguish between database cluster or namespaces.",
                gridPos=GridPos(h=8, w=4, x=16, y=66),
                id=769,
                targets=[
                    {
                        "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                        "editorMode": "code",
                        "expr": 'max(controller_runtime_reconcile_total{namespace=~"$operatorNamespace", '
                        'result="error", controller="pooler"})',
                        "hide": False,
                        "legendFormat": "Pooler Reconcile Errors",
                        "range": True,
                        "refId": "RECONCILE_ERRORS_BACKUP",
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
                            "mappings": [
                                {
                                    "options": {
                                        "0": {
                                            "color": "green",
                                            "index": 0,
                                            "text": "None",
                                        }
                                    },
                                    "type": "value",
                                },
                                {
                                    "options": {
                                        "from": 1,
                                        "result": {"color": "red", "index": 1},
                                        "to": 4294967295,
                                    },
                                    "type": "range",
                                },
                            ],
                            "thresholds": {
                                "mode": "absolute",
                                "steps": [{"color": "green"}],
                            },
                            "unitScale": True,
                        },
                        "overrides": [
                            {
                                "matcher": {"id": "byName", "options": "A"},
                                "properties": [
                                    {"id": "displayName", "value": "Reconcile errors"}
                                ],
                            }
                        ],
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
                    "pluginVersion": "10.3.3",
                },
            ),
        ],
    ),
]
