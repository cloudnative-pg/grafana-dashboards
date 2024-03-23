# Grafana Dashboards

![Grafana CloudNativePG Cluster Overview](charts/cluster/images/overview.png)

This repository contains the Grafana Dashboards distributed as Helm Charts so they can packaged as a dependency to other
projects.

## Dashboards

* [CloudNativePG Cluster Dashboard](charts/cluster/grafana-dashboard.json) 

## Repository

```bash
helm repo add cnpg-grafana https://cloudnative-pg.github.io/grafana-dashboards
```
### OCI Registry Example

If you want to use our OCI registry, signed by [cosign](https://github.com/sigstore/cosign), here is an example:

```bash
dependencies:
  - name: cnpg-grafana-cluster
    version: "0.0"
    repository: "oci://ghcr.io/cloudnative-pg/grafana-dashboards/cluster"
```

### Provenance

The charts support Helm Provenance and Integrity. 
Here is a link to the [PGP key](provenance.gpg) used by GitHub Actions to sign the charts.

## Contributing

Please read the [code of conduct](CODE-OF-CONDUCT.md) and the [guidelines](CONTRIBUTING.md) to contribute to the project.

## Copyright

Helm charts for CloudNativePG are distributed under [Apache License 2.0](LICENSE).
