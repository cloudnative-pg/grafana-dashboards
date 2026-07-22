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
| [operator_row.py](operator_row.py) | Operator |
| [cluster.dashboard.py](cluster.dashboard.py) | Entry point wiring every section together |

Every panel is transcribed **verbatim** (as plain Python data, not
grafanalib's typed panel classes) from the original JSON export. This
dashboard relies on many modern Grafana panel/fieldConfig features (value and
range mappings, per-field overrides, transformations, panel links, library
elements, ...) that grafanalib's higher-level classes (`Stat`, `TimeSeries`,
`GaugePanel`, ...) don't fully model, so building the panels through that
layer would risk silently changing behaviour. Using plain data keeps the
generated JSON byte-for-byte equivalent to the original while still using
grafanalib's project conventions and tooling to assemble and generate it.

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
