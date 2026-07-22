"""CloudNativePG cluster Grafana dashboard.

This is the grafanalib entry point that wires together every section of the
CloudNativePG cluster dashboard. Each section module builds its panels with
grafanalib's typed panel classes (``Stat``, ``TimeSeries``, ``Text``,
``RowPanel``, ...) plus the documented ``extraJson`` escape hatch for
fields those classes don't expose as constructor arguments, so no query,
threshold, mapping or option is lost. A few panel types (``alertlist``,
``gauge``, ``bargauge``, ``table``, ``heatmap``) are kept as plain dicts
instead, because grafanalib's class for them targets an older/incompatible
Grafana schema (see the ``NOTE:`` comments in the relevant section files).
This file only concatenates the sections in the right order and supplies
the dashboard's top-level metadata (templating, annotations, time range,
...). See ``README.md`` in this directory for the full rationale.

Regenerate ``../grafana-dashboard.json`` with:

    uv sync && uv run main.py
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from grafanalib.core import Annotations, Dashboard, Templating, Time

import sections.backups
import sections.checkpoints
import sections.collector_stats
import sections.configuration
import sections.extensions
import sections.operational_stats
import sections.operator
import sections.replication
import sections.server_health
import sections.storage_io
import sections.summary
import sections.write_ahead_log


# Every section module exposes a ``panels`` list containing the exact JSON
# (as Python data) of the top-level dashboard panels it is responsible for:
# either a handful of summary panels, or a single "row" panel (which embeds
# its children directly when collapsed, per Grafana's schema).
PANELS = (
    sections.summary.panels
    + sections.server_health.panels
    + sections.configuration.panels
    + sections.operational_stats.panels
    + sections.storage_io.panels
    + sections.write_ahead_log.panels
    + sections.replication.panels
    + sections.collector_stats.panels
    + sections.backups.panels
    + sections.checkpoints.panels
    + sections.extensions.panels
    + sections.operator.panels
)

dashboard = Dashboard(
    title="CloudNativePG",
    uid="cloudnative-pg",
    tags=["cloudnativepg"],
    editable=True,
    graphTooltip=1,
    refresh="30s",
    schemaVersion=39,
    timezone="",
    version=2,
    inputs=[
        {
            "name": "DS_PROMETHEUS",
            "label": "Prometheus",
            "description": "",
            "type": "datasource",
            "pluginId": "prometheus",
            "pluginName": "Prometheus",
        },
        {
            "name": "DS_EXPRESSION",
            "label": "Expression",
            "description": "",
            "type": "datasource",
            "pluginId": "__expr__",
        },
    ],
    annotations=Annotations(
        list=[
            {
                "builtIn": 1,
                "datasource": {"type": "datasource", "uid": "grafana"},
                "enable": True,
                "hide": True,
                "iconColor": "rgba(0, 211, 255, 1)",
                "name": "Annotations & Alerts",
                "target": {
                    "limit": 100,
                    "matchAny": False,
                    "tags": [],
                    "type": "dashboard",
                },
                "type": "dashboard",
            }
        ]
    ),
    links=[
        {
            "asDropdown": False,
            "icon": "external link",
            "includeVars": False,
            "keepTime": False,
            "tags": ["cloudnativepg"],
            "targetBlank": False,
            "title": "Related Dashboards",
            "tooltip": "",
            "type": "dashboards",
            "url": "",
        }
    ],
    templating=Templating(
        list=[
            {
                "current": {
                    "selected": False,
                    "text": "Prometheus",
                    "value": "prometheus",
                },
                "hide": 0,
                "includeAll": False,
                "label": "Datasource",
                "multi": False,
                "name": "DS_PROMETHEUS",
                "options": [],
                "query": "prometheus",
                "queryValue": "",
                "refresh": 1,
                "regex": "",
                "skipUrlSync": False,
                "type": "datasource",
            },
            {
                "current": {},
                "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                "definition": 'label_values(controller_runtime_webhook_requests_total{webhook="/mutate-postgresql-cnpg-io-v1-cluster"},namespace)',
                "description": "Namespace where the CNPG operator is located",
                "hide": 0,
                "includeAll": False,
                "label": "Operator Namespace",
                "multi": False,
                "name": "operatorNamespace",
                "options": [],
                "query": {
                    "qryType": 1,
                    "query": 'label_values(controller_runtime_webhook_requests_total{webhook="/mutate-postgresql-cnpg-io-v1-cluster"},namespace)',
                    "refId": "PrometheusVariableQueryEditor-VariableQuery",
                },
                "refresh": 2,
                "regex": "",
                "skipUrlSync": False,
                "sort": 0,
                "type": "query",
            },
            {
                "current": {},
                "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                "definition": "cnpg_collector_up",
                "description": "Namespace where the database cluster is located",
                "hide": 0,
                "includeAll": False,
                "label": "Database Namespace",
                "multi": False,
                "name": "namespace",
                "options": [],
                "query": {
                    "query": "cnpg_collector_up",
                    "refId": "StandardVariableQuery",
                },
                "refresh": 2,
                "regex": '/namespace="(?<text>[^"]+)/g',
                "skipUrlSync": False,
                "sort": 0,
                "type": "query",
            },
            {
                "current": {},
                "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                "definition": 'cnpg_collector_up{namespace=~"$namespace"}',
                "description": "CNPG Cluster",
                "hide": 0,
                "includeAll": False,
                "label": "Cluster",
                "multi": False,
                "name": "cluster",
                "options": [],
                "query": {
                    "query": 'cnpg_collector_up{namespace=~"$namespace"}',
                    "refId": "PrometheusVariableQueryEditor-VariableQuery",
                },
                "refresh": 2,
                "regex": '/\\bcluster\\b="(?<text>[^"]+)/g',
                "skipUrlSync": False,
                "sort": 1,
                "type": "query",
            },
            {
                "allValue": "$cluster-([1-9][0-9]*)",
                "current": {},
                "datasource": {"type": "prometheus", "uid": "${DS_PROMETHEUS}"},
                "definition": 'cnpg_collector_up{namespace=~"$namespace",pod=~"$cluster-([1-9][0-9]*)$"}',
                "description": "Database cluster instances",
                "hide": 0,
                "includeAll": True,
                "label": "Instances",
                "multi": True,
                "name": "instances",
                "options": [],
                "query": {
                    "qryType": 4,
                    "query": 'cnpg_collector_up{namespace=~"$namespace",pod=~"$cluster-([1-9][0-9]*)$"}',
                    "refId": "PrometheusVariableQueryEditor-VariableQuery",
                },
                "refresh": 2,
                "regex": '/pod="(?<text>[^"]+)/g',
                "skipUrlSync": False,
                "sort": 1,
                "type": "query",
            },
        ]
    ),
    time=Time("now-7d", "now"),
    panels=PANELS,
)
