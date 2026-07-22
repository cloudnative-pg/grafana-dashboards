"""Backups row (collapsed).

Transcribed verbatim from the original grafana-dashboard.json (panel indices 62-62).
"""

panels = [
    {
        "collapsed": True,
        "datasource": {"uid": "prometheus"},
        "gridPos": {"h": 1, "w": 24, "x": 0, "y": 55},
        "id": 239,
        "panels": [
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
                "gridPos": {"h": 6, "w": 8, "x": 0, "y": 56},
                "id": 237,
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
                        "expr": 'cnpg_collector_first_recoverability_point{namespace=~"$namespace",pod=~"$instances"}*1000 '
                        "> 0",
                        "format": "time_series",
                        "interval": "",
                        "legendFormat": "{{pod}}",
                        "refId": "A",
                    }
                ],
                "title": "First Recoverability Point",
                "type": "timeseries",
            }
        ],
        "targets": [{"datasource": {"uid": "prometheus"}, "refId": "A"}],
        "title": "Backups",
        "type": "row",
    }
]
