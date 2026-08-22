from __future__ import annotations
import argparse,json,re
from pathlib import Path
CHECKS={'run-as-non-root':'runAsNonRoot: true','no-priv-escalation':'allowPrivilegeEscalation: false','read-only-root':'readOnlyRootFilesystem: true','drop-caps':'drop: ["ALL"]','requests':'requests:','limits':'limits:','readiness':'readinessProbe:','liveness':'livenessProbe:','seccomp':'RuntimeDefault'}
def audit(text):
    findings=[name for name,needle in CHECKS.items() if needle not in text]
    if not re.search(r'image:\s*\S+@sha256:[0-9a-f]{64}',text): findings.append('digest-pinned-image')
    return {'passed':not findings,'checks':len(CHECKS)+1,'failed_controls':findings,'score_percent':round(100*(len(CHECKS)+1-len(findings))/(len(CHECKS)+1),1)}
def main():
    p=argparse.ArgumentParser(); p.add_argument('manifest',type=Path); p.add_argument('--output',type=Path,default=Path('artifacts/report.json')); a=p.parse_args(); report=audit(a.manifest.read_text()); a.output.parent.mkdir(parents=True,exist_ok=True); a.output.write_text(json.dumps(report,indent=2)); print(json.dumps(report,indent=2)); raise SystemExit(0 if report['passed'] else 1)
if __name__=='__main__': main()
