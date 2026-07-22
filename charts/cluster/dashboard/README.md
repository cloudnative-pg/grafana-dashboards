# CloudNativePG cluster dashboard (grafanalib)

This directory contains the [grafanalib](https://github.com/weaveworks/grafanalib)
source for `../grafana-dashboard.json`, split into one file per dashboard
section/row so it's easier to review and maintain:

| File | Dashboard section |
| --- | --- |
| [summary.py](summary.py) | Summary panels at the top (no row header) |
| [server_health.py](server_health.py) | Server Health |
| [configuration.py](configuration.py) | Configuration |
| [operational_stats.py](operational_stats.py) | Operational Stats |
| [storage_io.py](storage_io.py) | Storage & I/O |
| [write_ahead_log.py](write_ahead_log.py) | Write Ahead Log |
| [replication.py](replication.py) | Replication |
| [collector_stats.py](collector_stats.py) | Collector Stats |
| [backups.py](backups.py) | Backups |
| [checkpoints.py](checkpoints.py) | Checkpoints |
| [extensions.py](extensions.py) | Extensions |
| [operator.py](operator.py) | Operator |
| [cluster.dashboard.py](cluster.dashboard.py) | Entry point wiring every section together |

Every panel is built with grafanalib's typed panel classes (`Stat`,
`TimeSeries`, `Text`, `RowPanel`, `GridPos`, ...) where those classes cleanly
model this dashboard's modern (schemaVersion 39) panel/fieldConfig schema.
Fields those classes don't expose as constructor arguments (value/range
mappings, per-field overrides, transformations, axis/legend/tooltip options,
...) are passed through grafanalib's documented `extraJson` mechanism, which
deep-merges the exact original sub-structures on top of what the class
generates, so no query, threshold, mapping or option is lost or altered.

A handful of panel types are kept as plain dicts instead, because
grafanalib's class for them targets an older/incompatible Grafana schema and
has no way to reproduce the modern one (see the `NOTE:` comment above each):
`alertlist` (`AlertList` targets the legacy alert list schema and has no
`extraJson`), `gauge`/`bargauge` (`GaugePanel`/`BarGauge` still emit the
legacy single-stat `fieldOptions` shape), `table` (legacy top-level
`color`/`columns`/`mappings` shape) and `heatmap` (the old Angular heatmap
panel shape).

Because grafanalib's typed classes always emit their own fixed set of
default-valued fields (e.g. `cacheTimeout`, `error`, `transparent`,
`maxDataPoints`, empty `links`/`transformations`, ...) even when the original
export omits them, the regenerated JSON is a strict **superset** of the
original: every original key/value is preserved unchanged, but some
additional default-valued keys appear that Grafana already assumes anyway
when absent. This was verified panel-by-panel (recursive diff finding zero
missing or changed values, only additions) before adopting this approach.

## Regenerating the dashboard JSON

This is a [uv](https://docs.astral.sh/uv/) project. Regenerate
`../grafana-dashboard.json` with:

```shell
uv sync && uv run main.py
```

or, from the repository root:

```shell
make dashboard
```

This must be re-run (and the resulting `grafana-dashboard.json` committed)
whenever any file in this directory changes, since the Helm chart embeds the
generated JSON file directly (see `../templates/sidecar-configmap.yaml`).
