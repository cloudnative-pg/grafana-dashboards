"""Configuration row (collapsed).

Transcribed from the original grafana-dashboard.json (panel indices 49-49), rewritten
using grafanalib's typed panel classes where they cleanly model this dashboard's
(modern) panel schema. Panel types where grafanalib only models an older/incompatible
Grafana schema are kept as plain dicts (see inline notes).
"""

from grafanalib.core import GridPos, RowPanel, Stat, Text

panels = [
    RowPanel(
        title="Configuration",
        dataSource={"uid": "prometheus"},
        gridPos=GridPos(h=1, w=24, x=0, y=18),
        id=41,
        targets=[{"datasource": {"uid": "prometheus"}, "refId": "A"}],
        collapsed=True,
        panels=[
            Text(
                title="Instance",
                dataSource={"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                gridPos=GridPos(h=1, w=3, x=0, y=25),
                id=187,
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
                    "pluginVersion": "10.3.1",
                    "repeatDirection": "v",
                    "transparent": True,
                },
            ),
            Text(
                title="Max Connections",
                dataSource={"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                gridPos=GridPos(h=1, w=3, x=3, y=25),
                id=183,
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
                    "pluginVersion": "10.3.1",
                    "repeatDirection": "v",
                },
            ),
            Text(
                title="Shared Buffers",
                dataSource={"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                gridPos=GridPos(h=1, w=3, x=6, y=25),
                id=184,
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
                    "pluginVersion": "10.3.1",
                    "repeatDirection": "v",
                },
            ),
            Text(
                title="Effective Cache Size",
                dataSource={"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                gridPos=GridPos(h=1, w=3, x=9, y=25),
                id=185,
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
                    "pluginVersion": "10.3.1",
                    "repeatDirection": "v",
                },
            ),
            Text(
                title="Work Mem",
                dataSource={"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                gridPos=GridPos(h=1, w=3, x=12, y=25),
                id=186,
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
                    "pluginVersion": "10.3.1",
                    "repeatDirection": "v",
                },
            ),
            Text(
                title="Maintenance Work Mem",
                dataSource={"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                gridPos=GridPos(h=1, w=3, x=15, y=25),
                id=188,
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
                    "pluginVersion": "10.3.1",
                    "repeatDirection": "v",
                },
            ),
            Text(
                title="Random Page Cost",
                dataSource={"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                gridPos=GridPos(h=1, w=3, x=18, y=25),
                id=189,
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
                    "pluginVersion": "10.3.1",
                    "repeatDirection": "v",
                },
            ),
            Text(
                title="Sequential Page Cost",
                dataSource={"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                gridPos=GridPos(h=1, w=3, x=21, y=25),
                id=190,
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
                    "pluginVersion": "10.3.1",
                    "repeatDirection": "v",
                },
            ),
            Text(
                dataSource={"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                gridPos=GridPos(h=3, w=3, x=0, y=26),
                id=86,
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
                    "pluginVersion": "10.3.1",
                    "repeat": "instances",
                    "repeatDirection": "v",
                },
            ),
            Stat(
                dataSource={"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                gridPos=GridPos(h=3, w=3, x=3, y=26),
                id=30,
                targets=[
                    {
                        "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                        "exemplar": True,
                        "expr": 'cnpg_pg_settings_setting{name="max_connections",namespace=~"$namespace",pod=~"$instances"}',
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
                                "steps": [{"color": "dark-purple"}],
                            },
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
                    "pluginVersion": "10.3.1",
                    "repeat": "instances",
                    "repeatDirection": "v",
                },
            ),
            Stat(
                dataSource={"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                description="",
                gridPos=GridPos(h=3, w=3, x=6, y=26),
                id=24,
                targets=[
                    {
                        "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                        "exemplar": True,
                        "expr": "max by (pod) "
                        '(cnpg_pg_settings_setting{name="shared_buffers",namespace=~"$namespace",pod=~"$instances"}) '
                        "* max by (pod) "
                        '(cnpg_pg_settings_setting{name="block_size",namespace=~"$namespace",pod=~"$instances"})',
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
                                "steps": [{"color": "dark-purple"}],
                            },
                            "unit": "bytes",
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
                    "pluginVersion": "10.3.1",
                    "repeat": "instances",
                    "repeatDirection": "v",
                },
            ),
            Stat(
                dataSource={"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                description="",
                gridPos=GridPos(h=3, w=3, x=9, y=26),
                id=57,
                targets=[
                    {
                        "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                        "exemplar": True,
                        "expr": "max by (pod) "
                        '(cnpg_pg_settings_setting{name="effective_cache_size",namespace=~"$namespace",pod=~"$instances"}) '
                        "* max by (pod) "
                        '(cnpg_pg_settings_setting{name="block_size",namespace=~"$namespace",pod=~"$instances"})',
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
                                "steps": [{"color": "dark-purple"}],
                            },
                            "unit": "bytes",
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
                    "pluginVersion": "10.3.1",
                    "repeat": "instances",
                    "repeatDirection": "v",
                },
            ),
            Stat(
                dataSource={"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                description="",
                gridPos=GridPos(h=3, w=3, x=12, y=26),
                id=26,
                targets=[
                    {
                        "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                        "exemplar": True,
                        "expr": 'cnpg_pg_settings_setting{name="work_mem",namespace=~"$namespace",pod=~"$instances"} '
                        "* 1024",
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
                                "steps": [{"color": "dark-purple"}],
                            },
                            "unit": "bytes",
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
                    "pluginVersion": "10.3.1",
                    "repeat": "instances",
                    "repeatDirection": "v",
                },
            ),
            Stat(
                dataSource={"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                gridPos=GridPos(h=3, w=3, x=15, y=26),
                id=47,
                targets=[
                    {
                        "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                        "exemplar": True,
                        "expr": 'cnpg_pg_settings_setting{name="maintenance_work_mem",namespace=~"$namespace",pod=~"$instances"}',
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
                                "steps": [{"color": "dark-purple"}],
                            },
                            "unit": "bytes",
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
                    "pluginVersion": "10.3.1",
                    "repeat": "instances",
                    "repeatDirection": "v",
                },
            ),
            Stat(
                dataSource={"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                gridPos=GridPos(h=3, w=3, x=18, y=26),
                id=48,
                targets=[
                    {
                        "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                        "exemplar": True,
                        "expr": 'cnpg_pg_settings_setting{name="random_page_cost",namespace=~"$namespace",pod=~"$instances"}',
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
                                "steps": [{"color": "dark-purple"}],
                            },
                            "unit": "none",
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
                    "pluginVersion": "10.3.1",
                    "repeat": "instances",
                    "repeatDirection": "v",
                },
            ),
            Stat(
                dataSource={"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                gridPos=GridPos(h=3, w=3, x=21, y=26),
                id=56,
                targets=[
                    {
                        "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                        "exemplar": True,
                        "expr": 'cnpg_pg_settings_setting{name="seq_page_cost",namespace=~"$namespace",pod=~"$instances"}',
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
                                "steps": [{"color": "dark-purple"}],
                            },
                            "unit": "none",
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
                    "pluginVersion": "10.3.1",
                    "repeat": "instances",
                    "repeatDirection": "v",
                },
            ),
            # NOTE: kept as a raw dict -- grafanalib's Table class emits a legacy top-level 'color'/'columns'/'mappings' shape that predates this panel's modern fieldConfig-based schema.
            {
                "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                "fieldConfig": {
                    "defaults": {
                        "color": {"mode": "thresholds"},
                        "custom": {
                            "align": "auto",
                            "cellOptions": {"type": "auto"},
                            "filterable": True,
                            "inspect": False,
                        },
                        "mappings": [],
                        "thresholds": {
                            "mode": "absolute",
                            "steps": [{"color": "dark-purple"}],
                        },
                        "unitScale": True,
                    },
                    "overrides": [],
                },
                "gridPos": {"h": 9, "w": 24, "x": 0, "y": 32},
                "id": 150,
                "options": {
                    "cellHeight": "sm",
                    "footer": {
                        "countRows": False,
                        "fields": "",
                        "reducer": ["sum"],
                        "show": False,
                    },
                    "showHeader": True,
                    "sortBy": [],
                },
                "pluginVersion": "10.3.1",
                "repeatDirection": "v",
                "targets": [
                    {
                        "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                        "exemplar": True,
                        "expr": 'cnpg_pg_settings_setting{namespace=~"$namespace",pod=~"$instances"}',
                        "format": "table",
                        "instant": True,
                        "interval": "",
                        "legendFormat": "{{pod}}",
                        "refId": "A",
                    }
                ],
                "title": "Configurations",
                "transformations": [
                    {
                        "id": "organize",
                        "options": {
                            "excludeByName": {
                                "Time": True,
                                "__name__": True,
                                "container": True,
                                "endpoint": True,
                                "instance": True,
                                "job": True,
                                "name": False,
                                "namespace": True,
                                "pod": False,
                            },
                            "indexByName": {
                                "Time": 0,
                                "Value": 9,
                                "__name__": 1,
                                "container": 2,
                                "endpoint": 3,
                                "instance": 4,
                                "job": 5,
                                "name": 7,
                                "namespace": 8,
                                "pod": 6,
                            },
                            "renameByName": {"__name__": "", "name": "parameter"},
                        },
                    },
                    {
                        "id": "groupingToMatrix",
                        "options": {
                            "columnField": "pod",
                            "rowField": "parameter",
                            "valueField": "Value",
                        },
                    },
                    {
                        "id": "organize",
                        "options": {
                            "excludeByName": {},
                            "indexByName": {},
                            "renameByName": {"parameter\\pod": "parameter"},
                        },
                    },
                ],
                "type": "table",
            },
        ],
    ),
]
