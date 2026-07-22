"""Storage & I/O row (collapsed).

Transcribed verbatim from the original grafana-dashboard.json (panel indices 58-58).
"""

panels = [
    {
        "collapsed": True,
        "datasource": {"uid": "prometheus"},
        "gridPos": {"h": 1, "w": 24, "x": 0, "y": 51},
        "id": 35,
        "panels": [
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
                                {"color": "green"},
                                {"color": "#EAB839", "value": 0.7},
                                {"color": "red", "value": 0.8},
                            ],
                        },
                        "unit": "percentunit",
                        "unitScale": True,
                    },
                    "overrides": [],
                },
                "gridPos": {"h": 8, "w": 12, "x": 0, "y": 52},
                "id": 424,
                "options": {
                    "minVizHeight": 75,
                    "minVizWidth": 75,
                    "orientation": "auto",
                    "reduceOptions": {
                        "calcs": ["lastNotNull"],
                        "fields": "",
                        "values": False,
                    },
                    "showThresholdLabels": False,
                    "showThresholdMarkers": True,
                    "sizing": "auto",
                    "text": {},
                },
                "pluginVersion": "10.3.3",
                "targets": [
                    {
                        "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                        "editorMode": "code",
                        "expr": "max by(persistentvolumeclaim) (1 - "
                        'kubelet_volume_stats_available_bytes{namespace="$namespace", '
                        'persistentvolumeclaim=~"$instances"} / '
                        'kubelet_volume_stats_capacity_bytes{namespace="$namespace", '
                        'persistentvolumeclaim=~"$instances"})',
                        "format": "time_series",
                        "interval": "",
                        "legendFormat": "{{persistentvolumeclaim}}",
                        "range": True,
                        "refId": "FREE_SPACE",
                    },
                    {
                        "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                        "editorMode": "code",
                        "expr": "max by(persistentvolumeclaim) (1 - "
                        'kubelet_volume_stats_available_bytes{namespace="$namespace", '
                        'persistentvolumeclaim=~"(${instances})-wal"} / '
                        'kubelet_volume_stats_capacity_bytes{namespace="$namespace", '
                        'persistentvolumeclaim=~"(${instances})-wal"})',
                        "format": "time_series",
                        "interval": "",
                        "legendFormat": "{{persistentvolumeclaim}}",
                        "range": True,
                        "refId": "FREE_SPACE_WAL",
                    },
                ],
                "title": "Volume Space Usage: PGDATA and WAL",
                "transformations": [],
                "type": "gauge",
            },
            {
                "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                "fieldConfig": {
                    "defaults": {
                        "color": {"mode": "thresholds"},
                        "decimals": 2,
                        "mappings": [],
                        "max": 1,
                        "min": 0,
                        "thresholds": {
                            "mode": "absolute",
                            "steps": [
                                {"color": "green"},
                                {"color": "#EAB839", "value": 0.8},
                                {"color": "red", "value": 0.9},
                            ],
                        },
                        "unit": "percentunit",
                        "unitScale": True,
                    },
                    "overrides": [],
                },
                "gridPos": {"h": 8, "w": 12, "x": 12, "y": 52},
                "id": 426,
                "options": {
                    "minVizHeight": 75,
                    "minVizWidth": 75,
                    "orientation": "auto",
                    "reduceOptions": {
                        "calcs": ["lastNotNull"],
                        "fields": "",
                        "values": False,
                    },
                    "showThresholdLabels": False,
                    "showThresholdMarkers": True,
                    "sizing": "auto",
                },
                "pluginVersion": "10.3.3",
                "targets": [
                    {
                        "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                        "editorMode": "code",
                        "expr": "max by(persistentvolumeclaim) "
                        '(kubelet_volume_stats_inodes_used{namespace="$namespace", '
                        'persistentvolumeclaim=~"$instances"} / '
                        'kubelet_volume_stats_inodes{namespace="$namespace", '
                        'persistentvolumeclaim=~"$instances"})',
                        "format": "time_series",
                        "interval": "",
                        "legendFormat": "{{persistentvolumeclaim}}",
                        "range": True,
                        "refId": "FREE_INODES",
                    },
                    {
                        "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                        "editorMode": "code",
                        "expr": "max by(persistentvolumeclaim) "
                        '(kubelet_volume_stats_inodes_used{namespace="$namespace", '
                        'persistentvolumeclaim=~"(${instances})-wal"} / '
                        'kubelet_volume_stats_inodes{namespace="$namespace", '
                        'persistentvolumeclaim=~"(${instances})-wal"})',
                        "format": "time_series",
                        "interval": "",
                        "legendFormat": "{{persistentvolumeclaim}}",
                        "range": True,
                        "refId": "FREE_INODES_WAL",
                    },
                ],
                "title": "Volume Inode Usage: PGDATA and WAL",
                "transformations": [],
                "type": "gauge",
            },
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
                                {"color": "green"},
                                {"color": "#EAB839", "value": 0.7},
                                {"color": "red", "value": 0.8},
                            ],
                        },
                        "unit": "percentunit",
                        "unitScale": True,
                    },
                    "overrides": [],
                },
                "gridPos": {"h": 7, "w": 24, "x": 0, "y": 60},
                "id": 564,
                "options": {
                    "minVizHeight": 75,
                    "minVizWidth": 75,
                    "orientation": "auto",
                    "reduceOptions": {
                        "calcs": ["lastNotNull"],
                        "fields": "",
                        "values": False,
                    },
                    "showThresholdLabels": False,
                    "showThresholdMarkers": True,
                    "sizing": "auto",
                    "text": {},
                },
                "pluginVersion": "10.3.3",
                "targets": [
                    {
                        "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                        "editorMode": "code",
                        "expr": "sum by (namespace,persistentvolumeclaim) "
                        '(kubelet_volume_stats_used_bytes{namespace="$namespace", '
                        'persistentvolumeclaim=~"(${instances})-tbs.*"}) \n'
                        "/\n"
                        "sum by (namespace,persistentvolumeclaim) "
                        '(kubelet_volume_stats_capacity_bytes{namespace="$namespace", '
                        'persistentvolumeclaim=~"(${instances})-tbs.*"}) \n'
                        "*\n"
                        "on(namespace, persistentvolumeclaim) group_left(volume,pod)\n"
                        'kube_pod_spec_volumes_persistentvolumeclaims_info{pod=~"$instances"}',
                        "format": "time_series",
                        "interval": "",
                        "legendFormat": "{{volume}}-{{pod}}",
                        "range": True,
                        "refId": "FREE_SPACE",
                    }
                ],
                "title": "Volume Space Usage: Tablespaces",
                "transformations": [],
                "type": "gauge",
            },
            {
                "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
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
                "gridPos": {"h": 8, "w": 12, "x": 0, "y": 67},
                "id": 44,
                "options": {
                    "legend": {
                        "calcs": [],
                        "displayMode": "list",
                        "placement": "bottom",
                        "showLegend": True,
                    },
                    "tooltip": {"mode": "multi", "sort": "none"},
                },
                "targets": [
                    {
                        "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                        "editorMode": "code",
                        "exemplar": True,
                        "expr": 'sum(rate(cnpg_pg_stat_database_tup_deleted{datname="",namespace=~"$namespace",pod=~"$instances"}[5m]))',
                        "interval": "",
                        "legendFormat": "deleted",
                        "range": True,
                        "refId": "A",
                    },
                    {
                        "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                        "editorMode": "code",
                        "exemplar": True,
                        "expr": 'sum(rate(cnpg_pg_stat_database_tup_inserted{datname="",namespace=~"$namespace",pod=~"$instances"}[5m]))',
                        "hide": False,
                        "interval": "",
                        "legendFormat": "inserted",
                        "range": True,
                        "refId": "B",
                    },
                    {
                        "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                        "editorMode": "code",
                        "exemplar": True,
                        "expr": 'sum(rate(cnpg_pg_stat_database_tup_fetched{datname="",namespace=~"$namespace",pod=~"$instances"}[5m]))',
                        "hide": False,
                        "interval": "",
                        "legendFormat": "fetched",
                        "range": True,
                        "refId": "C",
                    },
                    {
                        "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                        "editorMode": "code",
                        "exemplar": True,
                        "expr": 'sum(rate(cnpg_pg_stat_database_tup_returned{datname="",namespace=~"$namespace",pod=~"$instances"}[5m]))',
                        "hide": False,
                        "interval": "",
                        "legendFormat": "returned",
                        "range": True,
                        "refId": "D",
                    },
                    {
                        "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                        "editorMode": "code",
                        "exemplar": True,
                        "expr": 'sum(rate(cnpg_pg_stat_database_tup_updated{datname="",namespace=~"$namespace",pod=~"$instances"}[5m]))',
                        "hide": False,
                        "interval": "",
                        "legendFormat": "updated",
                        "range": True,
                        "refId": "E",
                    },
                ],
                "title": "Tuple I/O [5m]",
                "type": "timeseries",
            },
            {
                "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
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
                "gridPos": {"h": 8, "w": 12, "x": 12, "y": 67},
                "id": 46,
                "options": {
                    "legend": {
                        "calcs": [],
                        "displayMode": "list",
                        "placement": "bottom",
                        "showLegend": True,
                    },
                    "tooltip": {"mode": "multi", "sort": "none"},
                },
                "targets": [
                    {
                        "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                        "editorMode": "code",
                        "exemplar": True,
                        "expr": 'rate(cnpg_pg_stat_database_blks_hit{datname="",namespace=~"$namespace",pod=~"$instances"}[5m])',
                        "interval": "",
                        "legendFormat": "hit ({{pod}})",
                        "range": True,
                        "refId": "A",
                    },
                    {
                        "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                        "editorMode": "code",
                        "exemplar": True,
                        "expr": 'rate(cnpg_pg_stat_database_blks_read{datname="",namespace=~"$namespace",pod=~"$instances"}[5m])',
                        "hide": False,
                        "interval": "",
                        "legendFormat": "read ({{pod}})",
                        "range": True,
                        "refId": "B",
                    },
                ],
                "title": "Block I/O [5m]",
                "type": "timeseries",
            },
            {
                "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
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
                            "steps": [{"color": "green"}],
                        },
                        "unit": "decbytes",
                        "unitScale": True,
                    },
                    "overrides": [],
                },
                "gridPos": {"h": 8, "w": 12, "x": 0, "y": 75},
                "id": 22,
                "options": {
                    "legend": {
                        "calcs": [],
                        "displayMode": "list",
                        "placement": "bottom",
                        "showLegend": True,
                    },
                    "tooltip": {"mode": "multi", "sort": "none"},
                },
                "pluginVersion": "8.0.5",
                "targets": [
                    {
                        "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                        "editorMode": "code",
                        "exemplar": True,
                        "expr": "max by (datname) "
                        '(cnpg_pg_database_size_bytes{datname!~"template.*",datname!="postgres",namespace=~"$namespace",pod=~"$instances"})',
                        "interval": "",
                        "legendFormat": " {{pod}}: {{datname}}",
                        "range": True,
                        "refId": "A",
                    }
                ],
                "title": "Database Size",
                "type": "timeseries",
            },
            {
                "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
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
                        "unit": "decbytes",
                        "unitScale": True,
                    },
                    "overrides": [],
                },
                "gridPos": {"h": 8, "w": 12, "x": 12, "y": 75},
                "id": 2,
                "options": {
                    "legend": {
                        "calcs": [],
                        "displayMode": "list",
                        "placement": "bottom",
                        "showLegend": True,
                    },
                    "tooltip": {"mode": "multi", "sort": "none"},
                },
                "targets": [
                    {
                        "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                        "exemplar": True,
                        "expr": 'rate(cnpg_pg_stat_database_temp_bytes{datname="",namespace=~"$namespace",pod=~"$instances"}[5m])',
                        "instant": False,
                        "interval": "",
                        "legendFormat": "{{pod}}",
                        "refId": "A",
                    }
                ],
                "title": "Temp Bytes [5m]",
                "type": "timeseries",
            },
        ],
        "targets": [{"datasource": {"uid": "prometheus"}, "refId": "A"}],
        "title": "Storage & I/O",
        "type": "row",
    }
]
