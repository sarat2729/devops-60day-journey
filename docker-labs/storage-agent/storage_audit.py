import shutil
import json
import os
from datetime import datetime, timezone

target_path = os.getenv("AUDIT_PATH", "/")
total, used, free = shutil.disk_usage(target_path)
gb = 1024 ** 3

report = {
    "service": "devops-storage-telemetry-agent",
    "timestamp_utc": datetime.now(timezone.utc).isoformat(),
    "audited_mount": target_path,
    "total_gb": round(total / gb, 2),
    "used_gb": round(used / gb, 2),
    "free_gb": round(free / gb, 2),
    "utilization_pct": round((used / total) * 100, 2)
}

print(json.dumps(report, indent=2))
