"""CloudNativePG cluster Grafana dashboard.

This is the grafanalib entry point that wires together every section of the
CloudNativePG cluster dashboard. It is intentionally *not* built from
grafanalib's typed panel classes (``Stat``, ``TimeSeries``, ``GaugePanel``,
etc.): this dashboard relies on many modern Grafana panel/fieldConfig
features (value/range mappings, per-field overrides, transformations,
library elements, panel links, ...) that those classes don't model, and
recreating them through that layer would risk silently changing the
dashboard. Instead, every panel is transcribed verbatim (as plain Python
data) from the original ``grafana-dashboard.json`` export, split by section/
row so it is easier to review and maintain, and this file only takes care of
concatenating the sections in the right order and supplying the dashboard's
top-level metadata (templating, annotations, time range, ...).

Regenerate ``../grafana-dashboard.json`` with:

    generate-dashboard -o ../grafana-dashboard.json cluster.dashboard.py

(requires ``pip install -r requirements.txt``)
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import backups
import checkpoints
import collector_stats
import configuration
import extensions
import operational_stats
import operator_row
import replication
import server_health
import storage_io
import summary
import write_ahead_log


class RawDashboard:
    """Adapts a plain ``dict`` to grafanalib's dashboard generation tooling.

    grafanalib's ``generate-dashboard``/``generate-dashboards`` CLIs (and the
    ``write_dashboard`` helper they use) only require the loaded ``dashboard``
    object to expose a ``to_json_data()`` method, so a thin wrapper around a
    plain dict is all that's needed to keep the emitted JSON an exact match
    for the original dashboard, including top-level fields (like
    ``__inputs``/``__elements``/``__requires``/``weekStart``/``liveNow``)
    that grafanalib's own ``core.Dashboard`` class does not support.
    """

    def __init__(self, data):
        self._data = data

    def to_json_data(self):
        return self._data


# Every section module exposes a ``panels`` list containing the exact JSON
# (as Python data) of the top-level dashboard panels it is responsible for:
# either a handful of summary panels, or a single "row" panel (which embeds
# its children directly when collapsed, per Grafana's schema).
PANELS = (
    summary.panels
    + server_health.panels
    + configuration.panels
    + operational_stats.panels
    + storage_io.panels
    + write_ahead_log.panels
    + replication.panels
    + collector_stats.panels
    + backups.panels
    + checkpoints.panels
    + extensions.panels
    + operator_row.panels
)

dashboard = RawDashboard(
    {
        "__inputs": [
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
        "__elements": {},
        "__requires": [
            {"type": "datasource", "id": "__expr__", "version": "1.0.0"},
            {"type": "panel", "id": "alertlist", "name": "Alert list", "version": ""},
            {"type": "panel", "id": "bargauge", "name": "Bar gauge", "version": ""},
            {"type": "panel", "id": "gauge", "name": "Gauge", "version": ""},
            {
                "type": "grafana",
                "id": "grafana",
                "name": "Grafana",
                "version": "10.3.3",
            },
            {"type": "panel", "id": "heatmap", "name": "Heatmap", "version": ""},
            {
                "type": "datasource",
                "id": "prometheus",
                "name": "Prometheus",
                "version": "1.0.0",
            },
            {"type": "panel", "id": "stat", "name": "Stat", "version": ""},
            {"type": "panel", "id": "table", "name": "Table", "version": ""},
            {"type": "panel", "id": "text", "name": "Text", "version": ""},
            {"type": "panel", "id": "timeseries", "name": "Time series", "version": ""},
        ],
        "annotations": {
            "list": [
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
        },
        "editable": True,
        "fiscalYearStartMonth": 0,
        "graphTooltip": 1,
        "id": None,
        "links": [
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
        "liveNow": False,
        "refresh": "30s",
        "revision": 1,
        "schemaVersion": 39,
        "tags": ["cloudnativepg"],
        "templating": {
            "list": [
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
        },
        "time": {"from": "now-7d", "to": "now"},
        "timepicker": {"nowDelay": ""},
        "timezone": "",
        "title": "CloudNativePG",
        "uid": "cloudnative-pg",
        "version": 2,
        "weekStart": "",
        "panels": PANELS,
    }
)
