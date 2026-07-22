"""Summary components at the top of the dashboard (no row header).

Transcribed from the original grafana-dashboard.json (panel indices 0-28), rewritten
using grafanalib's typed panel classes where they cleanly model this dashboard's
(modern) panel schema. Panel types where grafanalib only models an older/incompatible
Grafana schema are kept as plain dicts (see inline notes).
"""

from grafanalib.core import GridPos, Stat, Text

panels = [
    # NOTE: kept as a raw dict -- grafanalib's AlertList class targets Grafana's legacy (pre-8.x) alert list schema and has no extraJson escape hatch, so it cannot reproduce this panel's modern schema.
    {
        "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
        "gridPos": {"h": 7, "w": 3, "x": 0, "y": 0},
        "id": 676,
        "options": {
            "alertInstanceLabelFilter": '{namespace=~"$namespace",pod=~"$instances"}',
            "alertName": "",
            "dashboardAlerts": False,
            "folder": "",
            "groupBy": [],
            "groupMode": "default",
            "maxItems": 20,
            "sortOrder": 1,
            "stateFilter": {
                "error": True,
                "firing": True,
                "noData": False,
                "normal": True,
                "pending": True,
            },
            "viewMode": "list",
        },
        "title": "Alerts",
        "type": "alertlist",
    },
    Text(
        title="Health",
        dataSource={"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
        gridPos=GridPos(h=1, w=4, x=3, y=0),
        id=586,
        extraJson={
            "options": {
                "code": {
                    "language": "plaintext",
                    "showLineNumbers": False,
                    "showMiniMap": False,
                },
                "content": "",
                "mode": "markdown",
            },
            "pluginVersion": "10.3.3",
        },
    ),
    Text(
        title="Overview",
        dataSource={"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
        gridPos=GridPos(h=1, w=12, x=7, y=0),
        id=336,
        extraJson={
            "options": {
                "code": {
                    "language": "plaintext",
                    "showLineNumbers": False,
                    "showMiniMap": False,
                },
                "content": "",
                "mode": "markdown",
            },
            "pluginVersion": "10.3.3",
        },
    ),
    Text(
        title="Storage",
        dataSource={"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
        gridPos=GridPos(h=1, w=2, x=19, y=0),
        id=352,
        extraJson={
            "options": {
                "code": {
                    "language": "plaintext",
                    "showLineNumbers": False,
                    "showMiniMap": False,
                },
                "content": "",
                "mode": "markdown",
            },
            "pluginVersion": "10.3.3",
        },
    ),
    Text(
        title="Backups",
        dataSource={"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
        gridPos=GridPos(h=1, w=3, x=21, y=0),
        id=354,
        extraJson={
            "options": {
                "code": {
                    "language": "plaintext",
                    "showLineNumbers": False,
                    "showMiniMap": False,
                },
                "content": "",
                "mode": "markdown",
            },
            "pluginVersion": "10.3.3",
        },
    ),
    Stat(
        dataSource={"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
        description="Cluster Replication Health represents the availability of replica servers available to replace the primary in case of a failure.",
        gridPos=GridPos(h=2, w=2, x=3, y=1),
        id=585,
        targets=[
            {
                "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                "editorMode": "code",
                "expr": '(max(cnpg_pg_replication_streaming_replicas{namespace=~"$namespace", '
                'pod=~"$instances"}) - '
                'sum(cnpg_pg_replication_is_wal_receiver_up{namespace=~"$namespace", '
                'pod=~"$instances"})) + '
                '(clamp_max(max(cnpg_pg_replication_streaming_replicas{namespace=~"$namespace", '
                'pod=~"$instances"}), 1) - 1)',
                "legendFormat": "Replication",
                "range": True,
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
                                "-1": {"color": "red", "index": 0, "text": "None"},
                                "0": {"color": "green", "index": 1, "text": "Healthy"},
                            },
                            "type": "value",
                        },
                        {
                            "options": {
                                "from": 2,
                                "result": {
                                    "color": "orange",
                                    "index": 2,
                                    "text": "Degraded",
                                },
                                "to": 999,
                            },
                            "type": "range",
                        },
                    ],
                    "thresholds": {
                        "mode": "absolute",
                        "steps": [{"color": "green", "value": None}],
                    },
                    "unitScale": True,
                },
                "overrides": [],
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
                "textMode": "auto",
                "wideLayout": True,
            },
            "pluginVersion": "10.3.3",
        },
    ),
    Stat(
        dataSource={"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
        description="High lag indicates issue with replication. Network or storage interfaces may not have enough bandwidth to handle incoming traffic and replication at the same time.",
        gridPos=GridPos(h=2, w=1, x=5, y=1),
        id=590,
        targets=[
            {
                "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                "editorMode": "code",
                "expr": 'max(cnpg_pg_replication_lag{namespace=~"$namespace",pod=~"$instances"}) + '
                'max(cnpg_pg_stat_replication_write_lag_seconds{namespace=~"$namespace",pod=~"$instances"}) '
                "+ "
                'max(cnpg_pg_stat_replication_flush_lag_seconds{namespace=~"$namespace",pod=~"$instances"}) '
                "+ "
                'max(cnpg_pg_stat_replication_replay_lag_seconds{namespace=~"$namespace",pod=~"$instances"})',
                "hide": False,
                "instant": False,
                "legendFormat": "Lag",
                "range": True,
                "refId": "LAG",
            },
            {
                "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                "expr": "",
                "hide": False,
                "instant": False,
                "range": True,
                "refId": "A",
            },
        ],
        extraJson={
            "fieldConfig": {
                "defaults": {
                    "color": {"mode": "thresholds"},
                    "mappings": [
                        {
                            "options": {
                                "match": "null",
                                "result": {
                                    "color": "text",
                                    "index": 0,
                                    "text": "No data",
                                },
                            },
                            "type": "special",
                        },
                        {
                            "options": {
                                "from": 0,
                                "result": {
                                    "color": "green",
                                    "index": 1,
                                    "text": "Healthy",
                                },
                                "to": 0.1,
                            },
                            "type": "range",
                        },
                        {
                            "options": {
                                "from": 0.1,
                                "result": {
                                    "color": "yellow",
                                    "index": 2,
                                    "text": "Sub-second",
                                },
                                "to": 1,
                            },
                            "type": "range",
                        },
                        {
                            "options": {
                                "from": 1,
                                "result": {
                                    "color": "orange",
                                    "index": 3,
                                    "text": "Delayed",
                                },
                                "to": 5,
                            },
                            "type": "range",
                        },
                        {
                            "options": {
                                "from": 5,
                                "result": {"color": "red", "index": 4, "text": "High"},
                                "to": 4294967295,
                            },
                            "type": "range",
                        },
                    ],
                    "thresholds": {
                        "mode": "absolute",
                        "steps": [{"color": "green", "value": None}],
                    },
                    "unitScale": True,
                },
                "overrides": [],
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
        description="Low disk space or low inode count will result in data loss.",
        gridPos=GridPos(h=2, w=1, x=6, y=1),
        id=613,
        targets=[
            {
                "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                "editorMode": "code",
                "expr": "max((max(max by(persistentvolumeclaim) (1 - "
                'kubelet_volume_stats_available_bytes{namespace="$namespace", '
                'persistentvolumeclaim=~"$instances"} / '
                'kubelet_volume_stats_capacity_bytes{namespace="$namespace", '
                'persistentvolumeclaim=~"$instances"}))) OR (max by(persistentvolumeclaim) '
                '(kubelet_volume_stats_inodes_used{namespace="$namespace", '
                'persistentvolumeclaim=~"$instances"} / '
                'kubelet_volume_stats_inodes{namespace="$namespace", '
                'persistentvolumeclaim=~"$instances"})))',
                "hide": False,
                "legendFormat": "Storage",
                "range": True,
                "refId": "STORAGE",
            }
        ],
        extraJson={
            "fieldConfig": {
                "defaults": {
                    "color": {"mode": "thresholds"},
                    "mappings": [
                        {
                            "options": {
                                "match": "null",
                                "result": {
                                    "color": "text",
                                    "index": 0,
                                    "text": "No data",
                                },
                            },
                            "type": "special",
                        },
                        {
                            "options": {
                                "from": 0,
                                "result": {
                                    "color": "green",
                                    "index": 1,
                                    "text": "Healthy",
                                },
                                "to": 0.8,
                            },
                            "type": "range",
                        },
                        {
                            "options": {
                                "from": 0.8,
                                "result": {
                                    "color": "orange",
                                    "index": 2,
                                    "text": "Warning",
                                },
                                "to": 0.9,
                            },
                            "type": "range",
                        },
                        {
                            "options": {
                                "from": 0.9,
                                "result": {
                                    "color": "red",
                                    "index": 3,
                                    "text": "Critical",
                                },
                                "to": 0.98,
                            },
                            "type": "range",
                        },
                        {
                            "options": {
                                "from": 0.98,
                                "result": {
                                    "color": "red",
                                    "index": 4,
                                    "text": "Data Loss",
                                },
                                "to": 1,
                            },
                            "type": "range",
                        },
                        {
                            "options": {
                                "from": 1,
                                "result": {"color": "red", "index": 5, "text": "Full"},
                                "to": 4294967295,
                            },
                            "type": "range",
                        },
                    ],
                    "thresholds": {
                        "mode": "absolute",
                        "steps": [{"color": "green", "value": None}],
                    },
                    "unitScale": True,
                },
                "overrides": [],
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
        title="Last failover",
        dataSource={"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
        description="",
        gridPos=GridPos(h=3, w=2, x=7, y=1),
        id=338,
        targets=[
            {
                "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                "editorMode": "code",
                "exemplar": False,
                "expr": 'max(cnpg_pg_postmaster_start_time{namespace=~"$namespace",pod=~"$instances"})*1000',
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
            "transformations": [],
        },
    ),
    Stat(
        title="TPS",
        dataSource={"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
        gridPos=GridPos(h=6, w=2, x=9, y=1),
        id=342,
        targets=[
            {
                "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                "editorMode": "code",
                "exemplar": True,
                "expr": 'sum(rate(cnpg_pg_stat_database_xact_commit{namespace=~"$namespace",pod=~"$instances"}[$__interval])) '
                "+ "
                'sum(rate(cnpg_pg_stat_database_xact_rollback{namespace=~"$namespace",pod=~"$instances"}[$__interval]))',
                "interval": "",
                "legendFormat": "TPS",
                "range": True,
                "refId": "TPS",
            }
        ],
        extraJson={
            "fieldConfig": {
                "defaults": {
                    "color": {"mode": "thresholds"},
                    "mappings": [],
                    "thresholds": {
                        "mode": "absolute",
                        "steps": [{"color": "green", "value": None}],
                    },
                    "unitScale": True,
                },
                "overrides": [],
            },
            "interval": "1m",
            "options": {
                "colorMode": "value",
                "graphMode": "area",
                "justifyMode": "auto",
                "orientation": "auto",
                "reduceOptions": {
                    "calcs": ["lastNotNull"],
                    "fields": "",
                    "values": False,
                },
                "showPercentChange": False,
                "textMode": "auto",
                "wideLayout": True,
            },
            "pluginVersion": "10.3.3",
        },
    ),
    # NOTE: kept as a raw dict -- grafanalib's GaugePanel class still emits the legacy single-stat 'fieldConfig.defaults.calcs/override' shape, not the modern gauge panel schema used here.
    {
        "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
        "description": "CPU Utilisation from Requests",
        "fieldConfig": {
            "defaults": {
                "color": {"mode": "thresholds"},
                "mappings": [
                    {
                        "options": {
                            "match": "null",
                            "result": {
                                "color": "text",
                                "index": 0,
                                "text": "Missing " "request",
                            },
                        },
                        "type": "special",
                    }
                ],
                "max": 1,
                "min": 0,
                "thresholds": {
                    "mode": "absolute",
                    "steps": [
                        {"color": "green", "value": None},
                        {"color": "orange", "value": 0.8},
                        {"color": "red", "value": 0.9},
                    ],
                },
                "unit": "percentunit",
                "unitScale": True,
            },
            "overrides": [],
        },
        "gridPos": {"h": 4, "w": 2, "x": 11, "y": 1},
        "id": 344,
        "interval": "1m",
        "links": [],
        "options": {
            "minVizHeight": 75,
            "minVizWidth": 75,
            "orientation": "horizontal",
            "reduceOptions": {"calcs": ["mean"], "fields": "", "values": False},
            "showThresholdLabels": False,
            "showThresholdMarkers": True,
            "sizing": "auto",
        },
        "pluginVersion": "10.3.3",
        "targets": [
            {
                "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                "editorMode": "code",
                "expr": 'sum(node_namespace_pod_container:container_cpu_usage_seconds_total:sum_irate{namespace="$namespace", '
                'pod=~"$instances"}) / '
                'sum(kube_pod_container_resource_requests{job="kube-state-metrics",  '
                'namespace="$namespace", resource="cpu", pod=~"$instances"})',
                "format": "time_series",
                "instant": True,
                "intervalFactor": 2,
                "refId": "A",
            }
        ],
        "title": "CPU Utilisation",
        "type": "gauge",
    },
    # NOTE: kept as a raw dict -- grafanalib's GaugePanel class still emits the legacy single-stat 'fieldConfig.defaults.calcs/override' shape, not the modern gauge panel schema used here.
    {
        "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
        "description": "Memory Utilisation from Requests",
        "fieldConfig": {
            "defaults": {
                "color": {"mode": "thresholds"},
                "mappings": [
                    {
                        "options": {
                            "match": "null",
                            "result": {
                                "color": "text",
                                "index": 0,
                                "text": "Missing " "request",
                            },
                        },
                        "type": "special",
                    }
                ],
                "max": 1,
                "min": 0,
                "thresholds": {
                    "mode": "absolute",
                    "steps": [
                        {"color": "green", "value": None},
                        {"color": "orange", "value": 0.8},
                        {"color": "red", "value": 0.9},
                    ],
                },
                "unit": "percentunit",
                "unitScale": True,
            },
            "overrides": [],
        },
        "gridPos": {"h": 4, "w": 2, "x": 13, "y": 1},
        "id": 348,
        "interval": "1m",
        "links": [],
        "options": {
            "minVizHeight": 75,
            "minVizWidth": 75,
            "orientation": "horizontal",
            "reduceOptions": {"calcs": ["mean"], "fields": "", "values": False},
            "showThresholdLabels": False,
            "showThresholdMarkers": True,
            "sizing": "auto",
        },
        "pluginVersion": "10.3.3",
        "targets": [
            {
                "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                "editorMode": "code",
                "expr": 'sum(container_memory_working_set_bytes{job="kubelet", '
                'metrics_path="/metrics/cadvisor", '
                'namespace="$namespace",container!="", image!="", '
                'pod=~"$instances"}) / sum(max by(pod) '
                '(kube_pod_container_resource_requests{job="kube-state-metrics", '
                'namespace="$namespace", resource="memory", pod=~"$instances"}))',
                "format": "time_series",
                "instant": True,
                "intervalFactor": 2,
                "refId": "A",
            }
        ],
        "title": "Memory Utilisation",
        "type": "gauge",
    },
    Stat(
        title="Replication Lag",
        dataSource={"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
        gridPos=GridPos(h=3, w=2, x=15, y=1),
        id=465,
        targets=[
            {
                "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                "editorMode": "code",
                "exemplar": False,
                "expr": 'max(cnpg_pg_replication_lag{namespace=~"$namespace",pod=~"$instances"})',
                "instant": True,
                "legendFormat": "__auto",
                "range": False,
                "refId": "A",
            }
        ],
        extraJson={
            "fieldConfig": {
                "defaults": {
                    "color": {"mode": "thresholds"},
                    "mappings": [],
                    "max": 30,
                    "min": 0,
                    "thresholds": {
                        "mode": "absolute",
                        "steps": [
                            {"color": "green", "value": None},
                            {"color": "yellow", "value": 1},
                            {"color": "orange", "value": 10},
                            {"color": "red", "value": 20},
                        ],
                    },
                    "unit": "s",
                    "unitScale": True,
                },
                "overrides": [],
            },
            "options": {
                "colorMode": "value",
                "graphMode": "area",
                "justifyMode": "auto",
                "orientation": "auto",
                "reduceOptions": {
                    "calcs": ["lastNotNull"],
                    "fields": "",
                    "values": False,
                },
                "showPercentChange": False,
                "textMode": "auto",
                "wideLayout": True,
            },
            "pluginVersion": "10.3.3",
        },
    ),
    Stat(
        title="Write Lag",
        dataSource={"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
        gridPos=GridPos(h=3, w=2, x=17, y=1),
        id=467,
        targets=[
            {
                "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                "editorMode": "code",
                "expr": 'max(cnpg_pg_stat_replication_write_lag_seconds{namespace=~"$namespace",pod=~"$instances"})',
                "legendFormat": "__auto",
                "range": True,
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
                        "steps": [
                            {"color": "green", "value": None},
                            {"color": "yellow", "value": 1},
                            {"color": "orange", "value": 10},
                            {"color": "red", "value": 20},
                        ],
                    },
                    "unit": "s",
                    "unitScale": True,
                },
                "overrides": [],
            },
            "options": {
                "colorMode": "value",
                "graphMode": "area",
                "justifyMode": "auto",
                "orientation": "auto",
                "reduceOptions": {
                    "calcs": ["lastNotNull"],
                    "fields": "",
                    "values": False,
                },
                "showPercentChange": False,
                "textMode": "auto",
                "wideLayout": True,
            },
            "pluginVersion": "10.3.3",
        },
    ),
    # NOTE: kept as a raw dict -- grafanalib's GaugePanel class still emits the legacy single-stat 'fieldConfig.defaults.calcs/override' shape, not the modern gauge panel schema used here.
    {
        "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
        "fieldConfig": {
            "defaults": {
                "color": {"mode": "thresholds"},
                "mappings": [],
                "max": 1,
                "min": 0,
                "thresholds": {
                    "mode": "absolute",
                    "steps": [
                        {"color": "green", "value": None},
                        {"color": "orange", "value": 0.8},
                        {"color": "red", "value": 0.9},
                    ],
                },
                "unit": "percentunit",
                "unitScale": True,
            },
            "overrides": [],
        },
        "gridPos": {"h": 4, "w": 2, "x": 19, "y": 1},
        "id": 356,
        "options": {
            "minVizHeight": 75,
            "minVizWidth": 75,
            "orientation": "auto",
            "reduceOptions": {"calcs": ["lastNotNull"], "fields": "", "values": False},
            "showThresholdLabels": False,
            "showThresholdMarkers": True,
            "sizing": "auto",
        },
        "pluginVersion": "10.3.3",
        "targets": [
            {
                "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                "editorMode": "code",
                "exemplar": False,
                "expr": "max(max by(persistentvolumeclaim) (1 - "
                'kubelet_volume_stats_available_bytes{namespace="$namespace", '
                'persistentvolumeclaim=~"$instances"} / '
                'kubelet_volume_stats_capacity_bytes{namespace="$namespace", '
                'persistentvolumeclaim=~"$instances"}))',
                "format": "time_series",
                "instant": True,
                "interval": "",
                "legendFormat": "DATA",
                "range": False,
                "refId": "DATA",
            },
            {
                "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                "editorMode": "code",
                "exemplar": False,
                "expr": "max(max by(persistentvolumeclaim) (1 - "
                'kubelet_volume_stats_available_bytes{namespace="$namespace", '
                'persistentvolumeclaim=~"(${instances})-wal"} / '
                'kubelet_volume_stats_capacity_bytes{namespace="$namespace", '
                'persistentvolumeclaim=~"(${instances})-wal"}))',
                "format": "time_series",
                "instant": True,
                "interval": "",
                "legendFormat": "WAL",
                "range": False,
                "refId": "WAL",
            },
            {
                "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                "editorMode": "code",
                "exemplar": False,
                "expr": "max(\n"
                "    sum by (namespace,persistentvolumeclaim) "
                '(kubelet_volume_stats_used_bytes{namespace="$namespace", '
                'persistentvolumeclaim=~"(${instances})-tbs.*"}) \n'
                "    /\n"
                "    sum by (namespace,persistentvolumeclaim) "
                '(kubelet_volume_stats_capacity_bytes{namespace="$namespace", '
                'persistentvolumeclaim=~"(${instances})-tbs.*"}) \n'
                "    *\n"
                "    on(namespace, persistentvolumeclaim) group_left(volume)\n"
                "    "
                'kube_pod_spec_volumes_persistentvolumeclaims_info{pod=~"$instances"}\n'
                ")",
                "hide": False,
                "instant": True,
                "legendFormat": "Tablespaces (max)",
                "range": False,
                "refId": "Max Tablespace",
            },
        ],
        "title": "Volume Space Usage",
        "type": "gauge",
    },
    Stat(
        title="Last Base Backup",
        dataSource={"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
        description="Elapsed time since the last successful base backup.",
        gridPos=GridPos(h=2, w=3, x=21, y=1),
        id=360,
        targets=[
            {
                "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                "editorMode": "code",
                "exemplar": False,
                "expr": "-(time() - "
                'max({__name__=~"cnpg_collector_last_available_backup_timestamp|barman_cloud_cloudnative_pg_io_last_available_backup_timestamp",namespace="$namespace",pod=~"$instances"}))',
                "instant": True,
                "legendFormat": "__auto",
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
                                "from": 1,
                                "result": {
                                    "color": "semi-dark-orange",
                                    "index": 0,
                                    "text": "Invalid " "date",
                                },
                                "to": 1e42,
                            },
                            "type": "range",
                        },
                        {
                            "options": {
                                "from": -2147483648,
                                "result": {"color": "red", "index": 1, "text": "N/A"},
                                "to": -1577847600,
                            },
                            "type": "range",
                        },
                    ],
                    "thresholds": {
                        "mode": "absolute",
                        "steps": [
                            {"color": "green", "value": None},
                            {"color": "semi-dark-red", "value": -108000},
                            {"color": "semi-dark-orange", "value": -107999},
                            {"color": "#EAB839", "value": -89999},
                            {"color": "green", "value": -86399},
                        ],
                    },
                    "unit": "dtdurations",
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
                "textMode": "auto",
                "wideLayout": True,
            },
            "pluginVersion": "10.3.3",
        },
    ),
    Stat(
        dataSource={"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
        description="High resource usage (CPU, Memory, DB Connections)",
        gridPos=GridPos(h=2, w=4, x=3, y=3),
        id=591,
        targets=[
            {
                "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                "editorMode": "code",
                "expr": "(sum(node_namespace_pod_container:container_cpu_usage_seconds_total:sum_irate{ "
                'namespace="$namespace", pod=~"$instances"}) / '
                'sum(kube_pod_container_resource_requests{job="kube-state-metrics", '
                'namespace="$namespace", resource="cpu", pod=~"$instances"}))',
                "hide": False,
                "legendFormat": "CPU",
                "range": True,
                "refId": "CPU",
            },
            {
                "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                "editorMode": "code",
                "expr": '(sum(container_memory_working_set_bytes{job="kubelet", '
                'metrics_path="/metrics/cadvisor", namespace="$namespace",container!="", '
                'image!="", pod=~"$instances"}) / sum(max by(pod) '
                '(kube_pod_container_resource_requests{job="kube-state-metrics", '
                'namespace="$namespace", resource="memory", pod=~"$instances"})))',
                "hide": False,
                "instant": False,
                "legendFormat": "Memory",
                "range": True,
                "refId": "MEM",
            },
            {
                "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                "editorMode": "code",
                "expr": ' (max(sum by (pod) (cnpg_backends_total{namespace=~"$namespace", '
                'pod=~"$instances"}) / sum by (pod) '
                '(cnpg_pg_settings_setting{name="max_connections", namespace=~"$namespace", '
                'pod=~"$instances"})))',
                "hide": False,
                "instant": False,
                "legendFormat": "Connections",
                "range": True,
                "refId": "CONNS",
            },
        ],
        extraJson={
            "fieldConfig": {
                "defaults": {
                    "color": {"mode": "thresholds"},
                    "mappings": [
                        {
                            "options": {
                                "match": "null",
                                "result": {
                                    "color": "text",
                                    "index": 0,
                                    "text": "No data",
                                },
                            },
                            "type": "special",
                        },
                        {
                            "options": {
                                "from": 0,
                                "result": {
                                    "color": "green",
                                    "index": 1,
                                    "text": "Healthy",
                                },
                                "to": 0.8,
                            },
                            "type": "range",
                        },
                        {
                            "options": {
                                "from": 0.8,
                                "result": {
                                    "color": "orange",
                                    "index": 2,
                                    "text": "Warning",
                                },
                                "to": 0.9,
                            },
                            "type": "range",
                        },
                        {
                            "options": {
                                "from": 0.9,
                                "result": {
                                    "color": "red",
                                    "index": 3,
                                    "text": "Critical",
                                },
                                "to": 0.98,
                            },
                            "type": "range",
                        },
                        {
                            "options": {
                                "from": 0.98,
                                "result": {
                                    "color": "red",
                                    "index": 4,
                                    "text": "Data Loss",
                                },
                                "to": 999,
                            },
                            "type": "range",
                        },
                    ],
                    "thresholds": {
                        "mode": "absolute",
                        "steps": [{"color": "green", "value": None}],
                    },
                    "unitScale": True,
                },
                "overrides": [],
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
        title="Last archived WAL",
        dataSource={"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
        description="Computes the time since the last known WAL archival in the primary.\nWe ensure to ignore the metric in the replicas by using (1 - cnpg_pg_replication_in_recovery ) as a multiplicative factor. It will be 0 for replicas, 1 for the primary.",
        gridPos=GridPos(h=2, w=3, x=21, y=3),
        id=362,
        targets=[
            {
                "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                "editorMode": "code",
                "exemplar": False,
                "expr": "max((1 - "
                'cnpg_pg_replication_in_recovery{namespace=~"$namespace",pod=~"$instances"}) '
                "* (time() - "
                'timestamp(cnpg_pg_stat_archiver_seconds_since_last_archival{namespace=~"$namespace",pod=~"$instances"}) '
                "+\n"
                'cnpg_pg_stat_archiver_seconds_since_last_archival{namespace=~"$namespace",pod=~"$instances"}))',
                "format": "time_series",
                "instant": True,
                "interval": "",
                "legendFormat": "__auto",
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
                                "match": "null",
                                "result": {
                                    "color": "red",
                                    "index": 0,
                                    "text": "No " "backups",
                                },
                            },
                            "type": "special",
                        },
                        {
                            "options": {
                                "from": -1e22,
                                "result": {
                                    "color": "text",
                                    "index": 1,
                                    "text": "No data",
                                },
                                "to": 0,
                            },
                            "type": "range",
                        },
                    ],
                    "thresholds": {
                        "mode": "absolute",
                        "steps": [{"color": "green", "value": None}],
                    },
                    "unit": "dtdurations",
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
                "textMode": "auto",
                "wideLayout": True,
            },
            "pluginVersion": "10.3.3",
        },
    ),
    Stat(
        title="Version",
        dataSource={"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
        description="",
        gridPos=GridPos(h=3, w=2, x=7, y=4),
        id=340,
        targets=[
            {
                "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                "editorMode": "builder",
                "exemplar": False,
                "expr": 'cnpg_collector_postgres_version{namespace=~"$namespace",pod=~"$instances"}',
                "format": "table",
                "hide": False,
                "instant": True,
                "interval": "",
                "intervalFactor": 1,
                "legendFormat": "{{pod}}",
                "range": False,
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
            "repeatDirection": "v",
            "transformations": [],
        },
    ),
    Stat(
        title="Flush Lag",
        dataSource={"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
        gridPos=GridPos(h=3, w=2, x=15, y=4),
        id=466,
        targets=[
            {
                "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                "editorMode": "code",
                "expr": 'max(cnpg_pg_stat_replication_flush_lag_seconds{namespace=~"$namespace",pod=~"$instances"})',
                "legendFormat": "__auto",
                "range": True,
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
                        "steps": [
                            {"color": "green", "value": None},
                            {"color": "yellow", "value": 1},
                            {"color": "orange", "value": 10},
                            {"color": "red", "value": 20},
                        ],
                    },
                    "unit": "s",
                    "unitScale": True,
                },
                "overrides": [],
            },
            "options": {
                "colorMode": "value",
                "graphMode": "area",
                "justifyMode": "auto",
                "orientation": "auto",
                "reduceOptions": {
                    "calcs": ["lastNotNull"],
                    "fields": "",
                    "values": False,
                },
                "showPercentChange": False,
                "textMode": "auto",
                "wideLayout": True,
            },
            "pluginVersion": "10.3.3",
        },
    ),
    Stat(
        title="Replay Lag",
        dataSource={"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
        gridPos=GridPos(h=3, w=2, x=17, y=4),
        id=468,
        targets=[
            {
                "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                "editorMode": "code",
                "expr": 'max(cnpg_pg_stat_replication_replay_lag_seconds{namespace=~"$namespace",pod=~"$instances"})',
                "legendFormat": "__auto",
                "range": True,
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
                        "steps": [
                            {"color": "green", "value": None},
                            {"color": "yellow", "value": 1},
                            {"color": "orange", "value": 10},
                            {"color": "red", "value": 20},
                        ],
                    },
                    "unit": "s",
                    "unitScale": True,
                },
                "overrides": [],
            },
            "options": {
                "colorMode": "value",
                "graphMode": "area",
                "justifyMode": "auto",
                "orientation": "auto",
                "reduceOptions": {
                    "calcs": ["lastNotNull"],
                    "fields": "",
                    "values": False,
                },
                "showPercentChange": False,
                "textMode": "auto",
                "wideLayout": True,
            },
            "pluginVersion": "10.3.3",
        },
    ),
    Stat(
        dataSource={"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
        description="Base Backups are considered healthy when there has been at least one base backup in the last 24 hours.",
        gridPos=GridPos(h=2, w=1, x=3, y=5),
        id=588,
        targets=[
            {
                "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                "editorMode": "code",
                "expr": "time() - "
                'max({__name__=~"cnpg_collector_last_available_backup_timestamp|barman_cloud_cloudnative_pg_io_last_available_backup_timestamp",namespace="$namespace", '
                'pod=~"$instances"})',
                "legendFormat": "Backups",
                "range": True,
                "refId": "BACKUPS",
            }
        ],
        extraJson={
            "fieldConfig": {
                "defaults": {
                    "color": {"mode": "thresholds"},
                    "mappings": [
                        {
                            "options": {
                                "match": "null",
                                "result": {
                                    "color": "orange",
                                    "index": 0,
                                    "text": "None",
                                },
                            },
                            "type": "special",
                        },
                        {
                            "options": {
                                "from": 0,
                                "result": {
                                    "color": "green",
                                    "index": 1,
                                    "text": "Healthy",
                                },
                                "to": 90000,
                            },
                            "type": "range",
                        },
                        {
                            "options": {
                                "from": 90000,
                                "result": {
                                    "color": "orange",
                                    "index": 2,
                                    "text": "Degraded",
                                },
                                "to": 108000,
                            },
                            "type": "range",
                        },
                        {
                            "options": {
                                "from": 108000,
                                "result": {
                                    "color": "red",
                                    "index": 3,
                                    "text": "None " "recent",
                                },
                                "to": 4294967295,
                            },
                            "type": "range",
                        },
                    ],
                    "thresholds": {
                        "mode": "absolute",
                        "steps": [{"color": "green", "value": None}],
                    },
                    "unitScale": True,
                },
                "overrides": [
                    {
                        "matcher": {"id": "byName", "options": "WAL"},
                        "properties": [
                            {
                                "id": "mappings",
                                "value": [
                                    {
                                        "options": {
                                            "match": "null",
                                            "result": {
                                                "color": "orange",
                                                "index": 0,
                                                "text": "None",
                                            },
                                        },
                                        "type": "special",
                                    },
                                    {
                                        "options": {
                                            "from": 0,
                                            "result": {
                                                "color": "green",
                                                "index": 1,
                                                "text": "Healthy",
                                            },
                                            "to": 360,
                                        },
                                        "type": "range",
                                    },
                                    {
                                        "options": {
                                            "from": 360,
                                            "result": {
                                                "color": "orange",
                                                "index": 2,
                                                "text": "Delayed",
                                            },
                                            "to": 900,
                                        },
                                        "type": "range",
                                    },
                                    {
                                        "options": {
                                            "from": 900,
                                            "result": {
                                                "color": "red",
                                                "index": 3,
                                                "text": "Unsynced",
                                            },
                                            "to": 4294967295,
                                        },
                                        "type": "range",
                                    },
                                ],
                            }
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
        description="WAL is considered Healthy when the last WAL is 0min to 6min old, Delayed when it is less than 15min and Unsynced for >15min.",
        gridPos=GridPos(h=2, w=1, x=4, y=5),
        id=612,
        targets=[
            {
                "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                "editorMode": "code",
                "expr": 'max((1 - cnpg_pg_replication_in_recovery{namespace=~"$namespace", '
                'pod=~"$instances"}) * (time() - '
                'timestamp(cnpg_pg_stat_archiver_seconds_since_last_archival{namespace=~"$namespace", '
                'pod=~"$instances"}) +\n'
                'cnpg_pg_stat_archiver_seconds_since_last_archival{namespace=~"$namespace", '
                'pod=~"$instances"}))',
                "hide": False,
                "instant": False,
                "legendFormat": "WAL",
                "range": True,
                "refId": "WAL",
            }
        ],
        extraJson={
            "fieldConfig": {
                "defaults": {
                    "color": {"mode": "thresholds"},
                    "mappings": [
                        {
                            "options": {
                                "match": "null",
                                "result": {
                                    "color": "orange",
                                    "index": 0,
                                    "text": "None",
                                },
                            },
                            "type": "special",
                        },
                        {
                            "options": {
                                "from": 0,
                                "result": {
                                    "color": "green",
                                    "index": 1,
                                    "text": "Healthy",
                                },
                                "to": 360,
                            },
                            "type": "range",
                        },
                        {
                            "options": {
                                "from": 360,
                                "result": {
                                    "color": "orange",
                                    "index": 2,
                                    "text": "Delayed",
                                },
                                "to": 900,
                            },
                            "type": "range",
                        },
                        {
                            "options": {
                                "from": 900,
                                "result": {
                                    "color": "red",
                                    "index": 3,
                                    "text": "Unsynced",
                                },
                                "to": 4294967295,
                            },
                            "type": "range",
                        },
                    ],
                    "thresholds": {
                        "mode": "absolute",
                        "steps": [{"color": "green", "value": None}],
                    },
                    "unitScale": True,
                },
                "overrides": [
                    {
                        "matcher": {"id": "byName", "options": "WAL"},
                        "properties": [
                            {
                                "id": "mappings",
                                "value": [
                                    {
                                        "options": {
                                            "match": "null",
                                            "result": {
                                                "color": "orange",
                                                "index": 0,
                                                "text": "None",
                                            },
                                        },
                                        "type": "special",
                                    },
                                    {
                                        "options": {
                                            "from": 0,
                                            "result": {
                                                "color": "green",
                                                "index": 1,
                                                "text": "Healthy",
                                            },
                                            "to": 360,
                                        },
                                        "type": "range",
                                    },
                                    {
                                        "options": {
                                            "from": 360,
                                            "result": {
                                                "color": "orange",
                                                "index": 2,
                                                "text": "Delayed",
                                            },
                                            "to": 900,
                                        },
                                        "type": "range",
                                    },
                                    {
                                        "options": {
                                            "from": 900,
                                            "result": {
                                                "color": "red",
                                                "index": 3,
                                                "text": "Unsynced",
                                            },
                                            "to": 4294967295,
                                        },
                                        "type": "range",
                                    },
                                ],
                            }
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
        description="Online if there is at least one ready operator pod",
        gridPos=GridPos(h=2, w=1, x=5, y=5),
        id=589,
        targets=[
            {
                "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                "editorMode": "code",
                "expr": 'sum(kube_pod_status_ready{namespace="$operatorNamespace", '
                'pod=~"cloudnative-pg.+|cnpg-controller-manager.+", condition="true"})',
                "hide": False,
                "instant": True,
                "legendFormat": "Operator Status",
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
                                "0": {"color": "red", "index": 0, "text": "Failure"}
                            },
                            "type": "value",
                        },
                        {
                            "options": {
                                "from": 1,
                                "result": {
                                    "color": "green",
                                    "index": 1,
                                    "text": "Online",
                                },
                                "to": 99,
                            },
                            "type": "range",
                        },
                    ],
                    "thresholds": {
                        "mode": "absolute",
                        "steps": [{"color": "green", "value": None}],
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
        gridPos=GridPos(h=2, w=1, x=6, y=5),
        id=655,
        targets=[
            {
                "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                "editorMode": "code",
                "expr": 'clamp_max(max(controller_runtime_reconcile_total{namespace=~"$operatorNamespace", '
                'result="error", controller="backup"}), 1)',
                "hide": True,
                "legendFormat": "__auto",
                "range": True,
                "refId": "RECONCILE_ERRORS_BACKUP",
            },
            {
                "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                "editorMode": "code",
                "expr": 'clamp_max(max(controller_runtime_reconcile_total{namespace=~"$operatorNamespace", '
                'result="error", controller="cluster"}), 1)',
                "hide": True,
                "legendFormat": "__auto",
                "range": True,
                "refId": "RECONCILE_ERRORS_CLUSTER",
            },
            {
                "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                "editorMode": "code",
                "expr": 'clamp_max(max(controller_runtime_reconcile_total{namespace=~"$operatorNamespace", '
                'result="error", controller="pooler"}), 1)',
                "hide": True,
                "legendFormat": "__auto",
                "range": True,
                "refId": "RECONCILE_ERRORS_POOLER",
            },
            {
                "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                "editorMode": "code",
                "expr": 'clamp_max(max(controller_runtime_reconcile_total{namespace=~"$operatorNamespace", '
                'result="error", controller=~"scheduledbackup|scheduled-backup"}), 1)',
                "hide": True,
                "legendFormat": "__auto",
                "range": True,
                "refId": "RECONCILE_ERRORS_SCHEDULED_BACKUP",
            },
            {
                "datasource": {"type": "__expr__", "uid": "${DS_EXPRESSION}"},
                "expression": "$RECONCILE_ERRORS_BACKUP + $RECONCILE_ERRORS_CLUSTER * 10 + "
                "$RECONCILE_ERRORS_POOLER * 100 + $RECONCILE_ERRORS_SCHEDULED_BACKUP * "
                "1000",
                "hide": False,
                "refId": "A",
                "type": "math",
            },
        ],
        extraJson={
            "fieldConfig": {
                "defaults": {
                    "color": {"mode": "thresholds"},
                    "mappings": [
                        {
                            "options": {
                                "0": {"color": "green", "index": 0, "text": "None"}
                            },
                            "type": "value",
                        },
                        {
                            "options": {
                                "from": 1,
                                "result": {
                                    "color": "red",
                                    "index": 1,
                                    "text": "Backup",
                                },
                                "to": 9,
                            },
                            "type": "range",
                        },
                        {
                            "options": {
                                "from": 10,
                                "result": {
                                    "color": "red",
                                    "index": 2,
                                    "text": "Cluster",
                                },
                                "to": 99,
                            },
                            "type": "range",
                        },
                        {
                            "options": {
                                "from": 100,
                                "result": {
                                    "color": "red",
                                    "index": 3,
                                    "text": "Pooler",
                                },
                                "to": 999,
                            },
                            "type": "range",
                        },
                        {
                            "options": {
                                "from": 1000,
                                "result": {
                                    "color": "red",
                                    "index": 4,
                                    "text": "Scheduled " "Backup",
                                },
                                "to": 9999,
                            },
                            "type": "range",
                        },
                    ],
                    "thresholds": {
                        "mode": "absolute",
                        "steps": [{"color": "green", "value": None}],
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
        description="",
        gridPos=GridPos(h=2, w=2, x=11, y=5),
        id=346,
        targets=[
            {
                "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                "editorMode": "code",
                "exemplar": True,
                "expr": 'sum(node_namespace_pod_container:container_cpu_usage_seconds_total:sum_irate{namespace="$namespace", '
                'pod=~"$instances"})',
                "hide": False,
                "interval": "",
                "legendFormat": "Total",
                "range": True,
                "refId": "B",
            }
        ],
        extraJson={
            "fieldConfig": {
                "defaults": {
                    "color": {"mode": "thresholds"},
                    "decimals": 2,
                    "mappings": [],
                    "thresholds": {
                        "mode": "absolute",
                        "steps": [
                            {"color": "green", "value": None},
                            {"color": "#EAB839", "value": 80000000000},
                            {"color": "red", "value": 90000000000},
                        ],
                    },
                    "unit": "none",
                    "unitScale": True,
                },
                "overrides": [],
            },
            "links": [],
            "options": {
                "colorMode": "value",
                "graphMode": "area",
                "justifyMode": "center",
                "orientation": "horizontal",
                "reduceOptions": {
                    "calcs": ["lastNotNull"],
                    "fields": "",
                    "values": False,
                },
                "showPercentChange": False,
                "textMode": "auto",
                "wideLayout": True,
            },
            "pluginVersion": "10.3.3",
        },
    ),
    Stat(
        dataSource={"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
        description="Container memory working set",
        gridPos=GridPos(h=2, w=2, x=13, y=5),
        id=350,
        targets=[
            {
                "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                "editorMode": "code",
                "exemplar": True,
                "expr": 'sum(container_memory_working_set_bytes{pod=~"$instances", '
                'namespace="$namespace", container!="", image!=""})',
                "hide": False,
                "interval": "",
                "legendFormat": "Total",
                "range": True,
                "refId": "B",
            }
        ],
        extraJson={
            "fieldConfig": {
                "defaults": {
                    "color": {"mode": "thresholds"},
                    "mappings": [],
                    "thresholds": {
                        "mode": "absolute",
                        "steps": [
                            {"color": "green", "value": None},
                            {"color": "#EAB839", "value": 80000000000},
                            {"color": "red", "value": 90000000000},
                        ],
                    },
                    "unit": "bytes",
                    "unitScale": True,
                },
                "overrides": [],
            },
            "links": [],
            "options": {
                "colorMode": "value",
                "graphMode": "area",
                "justifyMode": "center",
                "orientation": "horizontal",
                "reduceOptions": {
                    "calcs": ["lastNotNull"],
                    "fields": "",
                    "values": False,
                },
                "showPercentChange": False,
                "textMode": "auto",
                "wideLayout": True,
            },
            "pluginVersion": "10.3.3",
        },
    ),
    Stat(
        title="Database Size",
        dataSource={"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
        description="",
        gridPos=GridPos(h=2, w=2, x=19, y=5),
        id=358,
        targets=[
            {
                "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                "editorMode": "code",
                "exemplar": False,
                "expr": 'cnpg_pg_database_size_bytes{namespace="$namespace", pod=~"$instances"}',
                "format": "table",
                "instant": False,
                "legendFormat": "__auto",
                "range": True,
                "refId": "A",
            }
        ],
        extraJson={
            "fieldConfig": {
                "defaults": {
                    "color": {"mode": "thresholds"},
                    "decimals": 2,
                    "mappings": [],
                    "thresholds": {
                        "mode": "absolute",
                        "steps": [
                            {"color": "green", "value": None},
                            {"color": "#EAB839", "value": 60000000000},
                            {"color": "red", "value": 80000000000},
                        ],
                    },
                    "unit": "decbytes",
                    "unitScale": True,
                },
                "overrides": [],
            },
            "links": [],
            "options": {
                "colorMode": "value",
                "graphMode": "none",
                "justifyMode": "auto",
                "orientation": "auto",
                "reduceOptions": {"calcs": ["sum"], "fields": "", "values": False},
                "showPercentChange": False,
                "textMode": "value",
                "wideLayout": True,
            },
            "pluginVersion": "10.3.3",
            "transformations": [
                {
                    "id": "groupBy",
                    "options": {
                        "fields": {
                            "Value": {
                                "aggregations": ["max"],
                                "operation": "aggregate",
                            },
                            "datname": {"aggregations": [], "operation": "groupby"},
                        }
                    },
                }
            ],
        },
    ),
    Stat(
        title="First Recoverability Point",
        dataSource={"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
        gridPos=GridPos(h=2, w=3, x=21, y=5),
        id=364,
        targets=[
            {
                "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                "editorMode": "code",
                "exemplar": False,
                "expr": 'max({__name__=~"cnpg_collector_first_recoverability_point|barman_cloud_cloudnative_pg_io_first_recoverability_point",namespace=~"$namespace",pod=~"$instances"})*1000',
                "format": "time_series",
                "instant": True,
                "interval": "",
                "legendFormat": "{{pod}}",
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
                                "0": {"color": "red", "index": 1, "text": "N/A"}
                            },
                            "type": "value",
                        },
                        {
                            "options": {
                                "match": "null",
                                "result": {
                                    "color": "red",
                                    "index": 0,
                                    "text": "No " "backups",
                                },
                            },
                            "type": "special",
                        },
                    ],
                    "thresholds": {
                        "mode": "absolute",
                        "steps": [{"color": "green", "value": None}],
                    },
                    "unit": "dateTimeAsIso",
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
                "textMode": "auto",
                "wideLayout": True,
            },
            "pluginVersion": "10.3.3",
        },
    ),
]
