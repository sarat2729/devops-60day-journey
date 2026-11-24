#!/usr/bin/env python3
import shutil
import json

total, used, free = shutil.disk_usage("/")
gb = 1024 ** 3

report = {
    "mount": "/",
    "total_gb": round(total / gb, 2),
    "used_gb": round(used / gb, 2),
    "free_gb": round(free / gb, 2)
}

print(json.dumps(report, indent=2))
