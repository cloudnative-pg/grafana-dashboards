"""Server Health row.

Transcribed from the original grafana-dashboard.json (panel indices 29-48), rewritten
using grafanalib's typed panel classes where they cleanly model this dashboard's
(modern) panel schema. Panel types where grafanalib only models an older/incompatible
Grafana schema are kept as plain dicts (see inline notes).
"""

from grafanalib.core import GridPos, RowPanel, Stat, Text, TimeSeries

panels = [
    RowPanel(
        title="Server Health",
        dataSource={"uid": "prometheus"},
        gridPos=GridPos(h=1, w=24, x=0, y=7),
        id=12,
        targets=[{"datasource": {"uid": "prometheus"}, "refId": "A"}],
        collapsed=False,
        panels=[],
    ),
    Text(
        title="Instance",
        dataSource={"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
        gridPos=GridPos(h=1, w=3, x=0, y=8),
        id=191,
        targets=[
            {
                "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                "exemplar": True,
                "expr": 'kube_pod_container_status_ready{container="postgres",namespace=~"$namespace",pod=~"$instances"}',
                "instant": True,
                "interval": "",
                "legendFormat": "{{pod}}",
                "refId": "A",
            }
        ],
        extraJson={
            "options": {
                "code": {
                    "language": "plaintext",
                    "showLineNumbers": False,
                    "showMiniMap": False,
                },
                "content": "",
                "mode": "html",
            },
            "pluginVersion": "10.3.3",
            "repeatDirection": "v",
            "transparent": True,
        },
    ),
    Text(
        title="Status",
        dataSource={"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
        gridPos=GridPos(h=1, w=2, x=3, y=8),
        id=192,
        targets=[
            {
                "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                "exemplar": True,
                "expr": 'kube_pod_container_status_ready{container="postgres",namespace=~"$namespace",pod=~"$instances"}',
                "instant": True,
                "interval": "",
                "legendFormat": "{{pod}}",
                "refId": "A",
            }
        ],
        extraJson={
            "options": {
                "code": {
                    "language": "plaintext",
                    "showLineNumbers": False,
                    "showMiniMap": False,
                },
                "content": "",
                "mode": "html",
            },
            "pluginVersion": "10.3.3",
            "repeatDirection": "v",
        },
    ),
    Text(
        title="Clustering / replicas",
        dataSource={"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
        gridPos=GridPos(h=1, w=3, x=5, y=8),
        id=193,
        targets=[
            {
                "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                "exemplar": True,
                "expr": 'kube_pod_container_status_ready{container="postgres",namespace=~"$namespace",pod=~"$instances"}',
                "instant": True,
                "interval": "",
                "legendFormat": "{{pod}}",
                "refId": "A",
            }
        ],
        extraJson={
            "options": {
                "code": {
                    "language": "plaintext",
                    "showLineNumbers": False,
                    "showMiniMap": False,
                },
                "content": "",
                "mode": "html",
            },
            "pluginVersion": "10.3.3",
            "repeatDirection": "v",
        },
    ),
    Text(
        title="Zone",
        dataSource={"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
        gridPos=GridPos(h=1, w=2, x=8, y=8),
        id=384,
        targets=[
            {
                "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                "exemplar": True,
                "expr": 'kube_pod_container_status_ready{container="postgres",namespace=~"$namespace",pod=~"$instances"}',
                "instant": True,
                "interval": "",
                "legendFormat": "{{pod}}",
                "refId": "A",
            }
        ],
        extraJson={
            "options": {
                "code": {
                    "language": "plaintext",
                    "showLineNumbers": False,
                    "showMiniMap": False,
                },
                "content": "",
                "mode": "html",
            },
            "pluginVersion": "10.3.3",
            "repeatDirection": "v",
        },
    ),
    Text(
        title="Connections",
        dataSource={"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
        gridPos=GridPos(h=1, w=4, x=10, y=8),
        id=195,
        targets=[
            {
                "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                "exemplar": True,
                "expr": 'kube_pod_container_status_ready{container="postgres",namespace=~"$namespace",pod=~"$instances"}',
                "instant": True,
                "interval": "",
                "legendFormat": "{{pod}}",
                "refId": "A",
            }
        ],
        extraJson={
            "options": {
                "code": {
                    "language": "plaintext",
                    "showLineNumbers": False,
                    "showMiniMap": False,
                },
                "content": "",
                "mode": "html",
            },
            "pluginVersion": "10.3.3",
            "repeatDirection": "v",
        },
    ),
    Text(
        title="Max Connections",
        dataSource={"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
        gridPos=GridPos(h=1, w=3, x=14, y=8),
        id=196,
        targets=[
            {
                "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                "exemplar": True,
                "expr": 'kube_pod_container_status_ready{container="postgres",namespace=~"$namespace",pod=~"$instances"}',
                "instant": True,
                "interval": "",
                "legendFormat": "{{pod}}",
                "refId": "A",
            }
        ],
        extraJson={
            "options": {
                "code": {
                    "language": "plaintext",
                    "showLineNumbers": False,
                    "showMiniMap": False,
                },
                "content": "",
                "mode": "html",
            },
            "pluginVersion": "10.3.3",
            "repeatDirection": "v",
        },
    ),
    Text(
        title="Wraparound",
        dataSource={"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
        description="",
        gridPos=GridPos(h=1, w=3, x=17, y=8),
        id=197,
        targets=[
            {
                "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                "exemplar": True,
                "expr": 'kube_pod_container_status_ready{container="postgres",namespace=~"$namespace",pod=~"$instances"}',
                "instant": True,
                "interval": "",
                "legendFormat": "{{pod}}",
                "refId": "A",
            }
        ],
        extraJson={
            "options": {
                "code": {
                    "language": "plaintext",
                    "showLineNumbers": False,
                    "showMiniMap": False,
                },
                "content": "",
                "mode": "html",
            },
            "pluginVersion": "10.3.3",
            "repeatDirection": "v",
        },
    ),
    Text(
        title="Started",
        dataSource={"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
        gridPos=GridPos(h=1, w=2, x=20, y=8),
        id=313,
        targets=[
            {
                "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                "exemplar": True,
                "expr": 'kube_pod_container_status_ready{container="postgres",namespace=~"$namespace",pod=~"$instances"}',
                "instant": True,
                "interval": "",
                "legendFormat": "{{pod}}",
                "refId": "A",
            }
        ],
        extraJson={
            "options": {
                "code": {
                    "language": "plaintext",
                    "showLineNumbers": False,
                    "showMiniMap": False,
                },
                "content": "",
                "mode": "html",
            },
            "pluginVersion": "10.3.3",
            "repeatDirection": "v",
        },
    ),
    Text(
        title="Version",
        dataSource={"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
        gridPos=GridPos(h=1, w=2, x=22, y=8),
        id=198,
        targets=[
            {
                "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                "exemplar": True,
                "expr": 'kube_pod_container_status_ready{container="postgres",namespace=~"$namespace",pod=~"$instances"}',
                "instant": True,
                "interval": "",
                "legendFormat": "{{pod}}",
                "refId": "A",
            }
        ],
        extraJson={
            "options": {
                "code": {
                    "language": "plaintext",
                    "showLineNumbers": False,
                    "showMiniMap": False,
                },
                "content": "",
                "mode": "html",
            },
            "pluginVersion": "10.3.3",
            "repeatDirection": "v",
        },
    ),
    Text(
        dataSource={"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
        gridPos=GridPos(h=3, w=3, x=0, y=9),
        id=61,
        targets=[
            {
                "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                "exemplar": True,
                "expr": 'kube_pod_container_status_ready{container="postgres",namespace=~"$namespace",pod=~"$instances"}',
                "instant": True,
                "interval": "",
                "legendFormat": "{{pod}}",
                "refId": "A",
            }
        ],
        extraJson={
            "options": {
                "code": {
                    "language": "plaintext",
                    "showLineNumbers": False,
                    "showMiniMap": False,
                },
                "content": '<table style="width:100%; height:100%;border:0px solid '
                'black;">\n'
                '  <td style="text-align: center;vertical-align: '
                'middle;border:0px solid black; "><p style="font-weight: '
                'bold;">$instances</p>\n'
                "  </td>\n"
                "</table>",
                "mode": "html",
            },
            "pluginVersion": "10.3.3",
            "repeat": "instances",
            "repeatDirection": "v",
        },
    ),
    Stat(
        dataSource={"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
        gridPos=GridPos(h=3, w=2, x=3, y=9),
        id=33,
        targets=[
            {
                "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                "editorMode": "code",
                "exemplar": True,
                "expr": 'min(kube_pod_container_status_ready{container="postgres",namespace=~"$namespace",pod=~"$instances"})',
                "instant": True,
                "interval": "",
                "legendFormat": "",
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
                                "0": {"index": 0, "text": "Down"},
                                "1": {"index": 1, "text": "Up"},
                            },
                            "type": "value",
                        }
                    ],
                    "thresholds": {
                        "mode": "absolute",
                        "steps": [
                            {"color": "dark-red", "value": None},
                            {"color": "green", "value": 1},
                        ],
                    },
                    "unitScale": True,
                },
                "overrides": [],
            },
            "options": {
                "colorMode": "background",
                "graphMode": "area",
                "justifyMode": "auto",
                "orientation": "auto",
                "reduceOptions": {
                    "calcs": ["lastNotNull"],
                    "fields": "",
                    "values": False,
                },
                "showPercentChange": False,
                "text": {},
                "textMode": "value",
                "wideLayout": True,
            },
            "pluginVersion": "10.3.3",
            "repeat": "instances",
            "repeatDirection": "v",
        },
    ),
    Stat(
        dataSource={"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
        description="",
        gridPos=GridPos(h=3, w=2, x=5, y=9),
        id=60,
        targets=[
            {
                "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                "exemplar": True,
                "expr": "1 - "
                'cnpg_pg_replication_in_recovery{namespace=~"$namespace",pod=~"$instances"} '
                "+ "
                'cnpg_pg_replication_is_wal_receiver_up{namespace=~"$namespace",pod=~"$instances"}',
                "instant": True,
                "interval": "",
                "legendFormat": "{{pod}}",
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
                                "0": {"color": "red", "index": 1, "text": "No"},
                                "1": {"color": "green", "index": 0, "text": "Yes"},
                            },
                            "type": "value",
                        }
                    ],
                    "noValue": "-",
                    "thresholds": {
                        "mode": "absolute",
                        "steps": [
                            {"color": "green", "value": None},
                            {"color": "red", "value": 80},
                        ],
                    },
                    "unitScale": True,
                },
                "overrides": [],
            },
            "options": {
                "colorMode": "background",
                "graphMode": "area",
                "justifyMode": "auto",
                "orientation": "auto",
                "reduceOptions": {
                    "calcs": ["lastNotNull"],
                    "fields": "",
                    "values": False,
                },
                "showPercentChange": False,
                "text": {},
                "textMode": "value",
                "wideLayout": True,
            },
            "pluginVersion": "10.3.3",
            "repeat": "instances",
            "repeatDirection": "v",
            "transformations": [],
        },
    ),
    Stat(
        dataSource={"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
        description="",
        gridPos=GridPos(h=3, w=1, x=7, y=9),
        id=229,
        targets=[
            {
                "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                "editorMode": "code",
                "exemplar": True,
                "expr": 'cnpg_pg_replication_streaming_replicas{namespace=~"$namespace", '
                'pod=~"$instances"}',
                "instant": True,
                "interval": "",
                "legendFormat": "{{pod}}",
                "refId": "A",
            }
        ],
        extraJson={
            "fieldConfig": {
                "defaults": {
                    "color": {"mode": "thresholds"},
                    "mappings": [],
                    "noValue": "-",
                    "thresholds": {
                        "mode": "absolute",
                        "steps": [
                            {"color": "green", "value": None},
                            {"color": "red", "value": 80},
                        ],
                    },
                    "unitScale": True,
                },
                "overrides": [],
            },
            "options": {
                "colorMode": "value",
                "graphMode": "none",
                "justifyMode": "auto",
                "orientation": "auto",
                "reduceOptions": {
                    "calcs": ["lastNotNull"],
                    "fields": "",
                    "values": False,
                },
                "showPercentChange": False,
                "text": {},
                "textMode": "value",
                "wideLayout": True,
            },
            "pluginVersion": "10.3.3",
            "repeat": "instances",
            "repeatDirection": "v",
            "transformations": [],
        },
    ),
    Stat(
        dataSource={"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
        description="This metric depends on exporting the: `topology.kubernetes.io/zone` label through kube-state-metrics (not enabled by default). Can be added by changing its configuration with:\n\n```yaml\nmetricLabelsAllowlist:\n  - nodes=[topology.kubernetes.io/zone]\n```",
        gridPos=GridPos(h=3, w=2, x=8, y=9),
        id=386,
        targets=[
            {
                "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                "editorMode": "code",
                "exemplar": True,
                "expr": 'kube_pod_info{namespace=~"$namespace", pod=~"$instances"} * '
                "on(node,instance) group_left(label_topology_kubernetes_io_zone) "
                "kube_node_labels",
                "format": "table",
                "instant": True,
                "interval": "",
                "legendFormat": "{{pod}}",
                "refId": "A",
            }
        ],
        extraJson={
            "fieldConfig": {
                "defaults": {
                    "color": {"mode": "thresholds"},
                    "mappings": [],
                    "thresholds": {
                        "mode": "absolute",
                        "steps": [{"color": "blue", "value": None}],
                    },
                    "unitScale": True,
                },
                "overrides": [],
            },
            "options": {
                "colorMode": "value",
                "graphMode": "none",
                "justifyMode": "auto",
                "orientation": "auto",
                "reduceOptions": {
                    "calcs": ["lastNotNull"],
                    "fields": "/^label_topology_kubernetes_io_zone$/",
                    "values": False,
                },
                "showPercentChange": False,
                "text": {"valueSize": 18},
                "textMode": "value",
                "wideLayout": True,
            },
            "pluginVersion": "10.3.3",
            "repeat": "instances",
            "repeatDirection": "v",
            "transformations": [],
        },
    ),
    TimeSeries(
        dataSource={"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
        gridPos=GridPos(h=3, w=4, x=10, y=9),
        id=58,
        targets=[
            {
                "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                "editorMode": "code",
                "exemplar": True,
                "expr": 'sum by (pod) (cnpg_backends_total{namespace=~"$namespace", '
                'pod=~"$instances"})',
                "instant": False,
                "interval": "",
                "legendFormat": "-",
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
                        "steps": [{"color": "green", "value": None}],
                    },
                    "unit": "short",
                    "unitScale": True,
                },
                "overrides": [],
            },
            "options": {
                "legend": {
                    "calcs": ["last", "mean"],
                    "displayMode": "list",
                    "placement": "bottom",
                    "showLegend": True,
                },
                "tooltip": {"mode": "multi", "sort": "none"},
            },
            "pluginVersion": "8.2.1",
            "repeat": "instances",
            "repeatDirection": "v",
        },
    ),
    # NOTE: kept as a raw dict -- grafanalib's GaugePanel class still emits the legacy single-stat 'fieldConfig.defaults.calcs/override' shape, not the modern gauge panel schema used here.
    {
        "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
        "description": "",
        "fieldConfig": {
            "defaults": {
                "color": {"mode": "thresholds"},
                "decimals": 0,
                "mappings": [],
                "max": 100,
                "min": 0,
                "noValue": "<1%",
                "thresholds": {
                    "mode": "absolute",
                    "steps": [
                        {"color": "green", "value": None},
                        {"color": "#EAB839", "value": 75},
                        {"color": "red", "value": 90},
                    ],
                },
                "unit": "percent",
                "unitScale": True,
            },
            "overrides": [],
        },
        "gridPos": {"h": 3, "w": 3, "x": 14, "y": 9},
        "id": 32,
        "options": {
            "minVizHeight": 75,
            "minVizWidth": 75,
            "orientation": "horizontal",
            "reduceOptions": {"calcs": ["last"], "fields": "", "values": False},
            "showThresholdLabels": False,
            "showThresholdMarkers": True,
            "sizing": "auto",
            "text": {},
        },
        "pluginVersion": "10.3.3",
        "repeat": "instances",
        "repeatDirection": "v",
        "targets": [
            {
                "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                "editorMode": "code",
                "exemplar": True,
                "expr": "100 * sum by (pod) "
                '(cnpg_backends_total{namespace=~"$namespace", '
                'pod=~"$instances"}) / sum by (pod) '
                '(cnpg_pg_settings_setting{name="max_connections", '
                'namespace=~"$namespace", pod=~"$instances"})',
                "instant": True,
                "interval": "",
                "legendFormat": "{{pod}}",
                "refId": "A",
            }
        ],
        "type": "gauge",
    },
    # NOTE: kept as a raw dict -- grafanalib's BarGauge class still emits the legacy 'options.fieldOptions' shape, not the modern bar gauge panel schema used here.
    {
        "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
        "fieldConfig": {
            "defaults": {
                "color": {"mode": "thresholds"},
                "mappings": [],
                "max": 2147483647,
                "min": 0,
                "thresholds": {
                    "mode": "absolute",
                    "steps": [
                        {"color": "green", "value": None},
                        {"color": "#EAB839", "value": 200000000},
                        {"color": "red", "value": 1000000000},
                    ],
                },
                "unit": "none",
                "unitScale": True,
            },
            "overrides": [],
        },
        "gridPos": {"h": 3, "w": 3, "x": 17, "y": 9},
        "id": 8,
        "options": {
            "displayMode": "lcd",
            "maxVizHeight": 300,
            "minVizHeight": 10,
            "minVizWidth": 0,
            "namePlacement": "auto",
            "orientation": "horizontal",
            "reduceOptions": {"calcs": ["lastNotNull"], "fields": "", "values": False},
            "showUnfilled": True,
            "sizing": "auto",
            "text": {},
            "valueMode": "color",
        },
        "pluginVersion": "10.3.3",
        "repeat": "instances",
        "repeatDirection": "v",
        "targets": [
            {
                "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                "editorMode": "code",
                "exemplar": True,
                "expr": 'max by (pod) (cnpg_pg_database_xid_age{namespace=~"$namespace", '
                'pod=~"$instances"})',
                "instant": True,
                "interval": "",
                "legendFormat": "{{pod}}",
                "refId": "A",
            }
        ],
        "type": "bargauge",
    },
    Stat(
        dataSource={"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
        description="",
        gridPos=GridPos(h=3, w=2, x=20, y=9),
        id=314,
        targets=[
            {
                "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                "editorMode": "code",
                "exemplar": False,
                "expr": 'cnpg_pg_postmaster_start_time{namespace=~"$namespace", '
                'pod=~"$instances"}*1000',
                "format": "time_series",
                "hide": False,
                "instant": True,
                "interval": "",
                "intervalFactor": 1,
                "legendFormat": "",
                "refId": "A",
            }
        ],
        extraJson={
            "fieldConfig": {
                "defaults": {
                    "color": {"mode": "thresholds"},
                    "mappings": [],
                    "thresholds": {
                        "mode": "absolute",
                        "steps": [{"color": "dark-blue", "value": None}],
                    },
                    "unit": "dateTimeFromNow",
                    "unitScale": True,
                },
                "overrides": [],
            },
            "options": {
                "colorMode": "background",
                "graphMode": "none",
                "justifyMode": "auto",
                "orientation": "horizontal",
                "reduceOptions": {
                    "calcs": ["lastNotNull"],
                    "fields": "",
                    "values": False,
                },
                "showPercentChange": False,
                "text": {},
                "textMode": "value",
                "wideLayout": True,
            },
            "pluginVersion": "10.3.3",
            "repeat": "instances",
            "repeatDirection": "v",
            "transformations": [],
        },
    ),
    Stat(
        dataSource={"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
        description="",
        gridPos=GridPos(h=3, w=2, x=22, y=9),
        id=42,
        targets=[
            {
                "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                "editorMode": "code",
                "exemplar": False,
                "expr": 'cnpg_collector_postgres_version{namespace=~"$namespace", pod=~"$instances"}',
                "format": "table",
                "hide": False,
                "instant": True,
                "interval": "",
                "intervalFactor": 1,
                "legendFormat": "{{pod}}",
                "refId": "A",
            }
        ],
        extraJson={
            "fieldConfig": {
                "defaults": {
                    "color": {"mode": "thresholds"},
                    "mappings": [],
                    "thresholds": {
                        "mode": "absolute",
                        "steps": [{"color": "dark-blue", "value": None}],
                    },
                    "unit": "string",
                    "unitScale": True,
                },
                "overrides": [],
            },
            "options": {
                "colorMode": "background",
                "graphMode": "none",
                "justifyMode": "auto",
                "orientation": "horizontal",
                "reduceOptions": {
                    "calcs": ["lastNotNull"],
                    "fields": "/^full$/",
                    "values": False,
                },
                "showPercentChange": False,
                "text": {},
                "textMode": "value",
                "wideLayout": True,
            },
            "pluginVersion": "10.3.3",
            "repeat": "instances",
            "repeatDirection": "v",
            "transformations": [],
        },
    ),
]
