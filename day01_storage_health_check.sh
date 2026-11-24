#!/bin/bash
# Enterprise Linux & Storage Health Diagnostic Script
echo "=== SYSTEM & STORAGE HEALTH REPORT ($(date)) ==="
echo "--- Host & Kernel ---"
uname -a
uptime

echo -e "\n--- Block Devices & Filesystem Usage ---"
lsblk -o NAME,SIZE,TYPE,MOUNTPOINT,FSTYPE
df -hT -x tmpfs -x devtmpfs

echo -e "\n--- Memory & Swap ---"
free -h

echo -e "\n--- Top 5 I/O or CPU Consuming Processes ---"
ps -eo pid,ppid,cmd,%mem,%cpu --sort=-%cpu | head -n 6
