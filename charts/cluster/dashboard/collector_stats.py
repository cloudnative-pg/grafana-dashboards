"""Collector Stats row (collapsed).

Transcribed verbatim from the original grafana-dashboard.json (panel indices 61-61).
"""

panels = [
    {
        "collapsed": True,
        "datasource": {"uid": "prometheus"},
        "gridPos": {"h": 1, "w": 24, "x": 0, "y": 54},
        "id": 231,
        "panels": [
            {
                "cards": {},
                "color": {
                    "cardColor": "#b4ff00",
                    "colorScale": "sqrt",
                    "colorScheme": "interpolateOranges",
                    "exponent": 0.5,
                    "mode": "spectrum",
                },
                "dataFormat": "timeseries",
                "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                "fieldConfig": {
                    "defaults": {
                        "custom": {
                            "hideFrom": {
                                "legend": False,
                                "tooltip": False,
                                "viz": False,
                            },
                            "scaleDistribution": {"type": "linear"},
                        },
                        "unitScale": True,
                    },
                    "overrides": [],
                },
                "gridPos": {"h": 8, "w": 12, "x": 0, "y": 55},
                "heatmap": {},
                "hideZeroBuckets": False,
                "highlightCards": True,
                "id": 233,
                "legend": {"show": False},
                "options": {
                    "calculate": True,
                    "calculation": {},
                    "cellGap": 2,
                    "cellValues": {},
                    "color": {
                        "exponent": 0.5,
                        "fill": "#b4ff00",
                        "mode": "scheme",
                        "reverse": False,
                        "scale": "exponential",
                        "scheme": "Oranges",
                        "steps": 128,
                    },
                    "exemplars": {"color": "rgba(255,0,255,0.7)"},
                    "filterValues": {"le": 1e-09},
                    "legend": {"show": False},
                    "rowsFrame": {"layout": "auto"},
                    "showValue": "never",
                    "tooltip": {
                        "mode": "single",
                        "showColorScale": False,
                        "yHistogram": False,
                    },
                    "yAxis": {"axisPlacement": "left", "reverse": False, "unit": "s"},
                },
                "pluginVersion": "10.3.3",
                "reverseYBuckets": False,
                "targets": [
                    {
                        "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                        "exemplar": True,
                        "expr": 'cnpg_collector_collection_duration_seconds{namespace=~"$namespace",pod=~"$instances"}',
                        "interval": "",
                        "legendFormat": "",
                        "refId": "A",
                    }
                ],
                "title": "Collection Duration",
                "tooltip": {"show": True, "showHistogram": False},
                "type": "heatmap",
                "xAxis": {"show": True},
                "yAxis": {"format": "s", "logBase": 1, "show": True},
                "yBucketBound": "auto",
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
                "gridPos": {"h": 8, "w": 12, "x": 12, "y": 55},
                "id": 235,
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
                        "expr": 'cnpg_collector_last_collection_error{namespace=~"$namespace",pod=~"$instances"}',
                        "interval": "",
                        "legendFormat": "{{pod}}",
                        "refId": "A",
                    }
                ],
                "title": "Errors",
                "type": "timeseries",
            },
        ],
        "targets": [{"datasource": {"uid": "prometheus"}, "refId": "A"}],
        "title": "Collector Stats",
        "type": "row",
    }
]
