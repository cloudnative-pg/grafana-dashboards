"""Extensions row (collapsed).

Transcribed verbatim from the original grafana-dashboard.json (panel indices 64-64).
"""

panels = [
    {
        "collapsed": True,
        "gridPos": {"h": 1, "w": 24, "x": 0, "y": 57},
        "id": 794,
        "panels": [
            {
                "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                "description": "Show the installed extensions and their versions",
                "fieldConfig": {
                    "defaults": {
                        "color": {"mode": "thresholds"},
                        "custom": {
                            "align": "auto",
                            "cellOptions": {"type": "auto", "wrapText": False},
                            "filterable": False,
                            "inspect": False,
                        },
                    },
                    "overrides": [
                        {
                            "matcher": {"id": "byName", "options": "Update Available"},
                            "properties": [
                                {"id": "unit", "value": "bool"},
                                {
                                    "id": "mappings",
                                    "value": [
                                        {
                                            "options": {
                                                "0": {
                                                    "color": "transparent",
                                                    "index": 1,
                                                },
                                                "1": {"color": "red", "index": 0},
                                            },
                                            "type": "value",
                                        }
                                    ],
                                },
                                {
                                    "id": "custom.cellOptions",
                                    "value": {
                                        "applyToRow": True,
                                        "mode": "gradient",
                                        "type": "color-background",
                                    },
                                },
                            ],
                        }
                    ],
                },
                "gridPos": {"h": 8, "w": 24, "x": 0, "y": 81},
                "id": 792,
                "options": {
                    "cellHeight": "sm",
                    "footer": {
                        "countRows": False,
                        "fields": "",
                        "reducer": ["sum"],
                        "show": False,
                    },
                    "showHeader": True,
                    "sortBy": [{"desc": False, "displayName": "Value"}],
                },
                "pluginVersion": "11.4.0",
                "targets": [
                    {
                        "disableTextWrap": False,
                        "exemplar": False,
                        "expr": 'max(cnpg_pg_extensions_update_available{pod=~"$instances", '
                        'namespace=~"$namespace"}) by (datname, extname, '
                        "default_version, installed_version)",
                        "format": "table",
                        "fullMetaSearch": False,
                        "includeNullMetadata": True,
                        "instant": True,
                        "interval": "",
                        "legendFormat": "__auto",
                        "range": False,
                        "refId": "A",
                        "useBackend": False,
                    }
                ],
                "title": "Installed extensions",
                "transformations": [
                    {
                        "id": "sortBy",
                        "options": {"fields": {}, "sort": [{"field": "extname"}]},
                    },
                    {
                        "id": "organize",
                        "options": {
                            "excludeByName": {"Time": True},
                            "indexByName": {
                                "Time": 0,
                                "extname": 1,
                                "datname": 2,
                                "default_version": 3,
                                "installed_version": 4,
                                "Value": 5,
                            },
                            "renameByName": {
                                "default_version": "Default " "Version",
                                "datname": "Database",
                                "extname": "Extension",
                                "installed_version": "Installed " "Version",
                                "Value": "Update Available",
                            },
                            "includeByName": {},
                        },
                    },
                ],
                "type": "table",
            }
        ],
        "title": "Extensions",
        "type": "row",
    }
]
