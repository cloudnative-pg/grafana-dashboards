<!-- THIS FILE IS AUTOMATICALLY GENERATED. Make changes to README.md.gotmpl instead. -->

# cluster

![Version: 0.0.1](https://img.shields.io/badge/Version-0.0.1-informational?style=flat-square) ![Type: application](https://img.shields.io/badge/Type-application-informational?style=flat-square) ![AppVersion: 1.16.0](https://img.shields.io/badge/AppVersion-1.16.0-informational?style=flat-square)

![Grafana CloudNativePG Cluster Overview](images/overview.png)

Getting Started
---------------

_**Note,** this dashboard is already included in the [CloudNativePG Operator Helm Chart][operator]._

There are 4 ways to use the CloudNativePG Grafana Cluster Dashboard:

0. Install the [CloudNativePG Operator Helm Chart][operator]

1. Install manually via [Grafana.com](https://grafana.com/grafana/dashboards/20417-cloudnativepg/).

2. Install manually via the [Grafana JSON](https://github.com/cloudnative-pg/grafana-dashboards/blob/main/charts/cluster/grafana-dashboard.json):

```
https://raw.githubusercontent.com/cloudnative-pg/grafana-dashboards/main/charts/cluster/grafana-dashboard.json
```

3. Install directly in your cluster as a Helm Chart:

```bash
helm repo add cnpg-grafana https://cloudnative-pg.github.io/grafana-dashboards
helm upgrade
  --install \
  --namespace monitoring \
  cnpg-grafana-cluster cnpg-grafana/cluster
```

2. As as a dependency to an existing chart:

```yaml
dependencies:
  - name: cluster
    alias: cnpg-grafana-cluster-dashboard
    version: "0.0"
    repository: https://cloudnative-pg.github.io/grafana-dashboards
```

## Values

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| fullnameOverride | string | `""` |  |
| grafanaDashboard.annotations | object | `{}` | Annotations that ConfigMaps can have to get configured in Grafana. |
| grafanaDashboard.configMapName | string | `"cnpg-grafana-dashboard"` | The name of the ConfigMap containing the dashboard. |
| grafanaDashboard.labels | object | `{}` | Labels that ConfigMaps should have to get configured in Grafana. |
| grafanaDashboard.namespace | string | `""` | Allows overriding the namespace where the ConfigMap will be created, defaulting to the same one as the Release. |
| grafanaDashboard.sidecarLabel | string | `"grafana_dashboard"` | Label that ConfigMaps should have to be loaded as dashboards. DEPRECATED: Use labels instead. |
| grafanaDashboard.sidecarLabelValue | string | `"1"` | Label value that ConfigMaps should have to be loaded as dashboards. DEPRECATED: Use labels instead. |
| nameOverride | string | `""` |  |

[operator]: https://github.com/cloudnative-pg/charts/tree/main/charts/cloudnative-pg