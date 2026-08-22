# Kubernetes Mission Security Auditor

Defensive static auditor for Kubernetes workloads supporting synthetic aerospace software. It checks manifests against a focused set of workload-hardening controls.

## Checks
- Non-root containers
- No privilege escalation
- Read-only root filesystem
- Dropped capabilities
- Resource requests/limits
- Health probes
- Seccomp RuntimeDefault
- Immutable digest-pinned images

Run `python k8s_audit.py examples/deployment.yaml --output artifacts/report.json` and `python -m unittest discover -s tests -v`.

Static validation only; it never connects to or modifies a cluster.