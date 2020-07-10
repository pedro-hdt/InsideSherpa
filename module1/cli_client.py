#!/usr/bin/python3

"""
JPMC Virtual SEP - InsideSherpa - Module 1
Pedro Teixeira - O734271

CLI client for the alerts package. See README for instructions, or try the 
--help flag
"""

import argparse
import sys
from alerts import AlertService

parser = argparse.ArgumentParser()
parser.add_argument("--cpu", metavar="-c", type=int, nargs='?',
    help="the CPU utilization limit for which no alert is issued",
    default=85, required=False)
parser.add_argument("--mem", metavar="-m", type=int, nargs='?',
    help="the memory utilization limit for which no alert is issued",
    default=75, required=False)
parser.add_argument("--disk", metavar="-d", type=int, nargs='?',
    help="the disk utilization limit for which no alert is issued",
    default=60, required=False)

args = parser.parse_args()

alert_service = AlertService(args.cpu, args.mem, args.disk)

try:
    while True:
        line = sys.stdin.readline().strip()
        if len(line) == 0:
            break
        print(alert_service.alert_me(line))
except (EOFError, KeyboardInterrupt):
    print("\nTerminating (EOF / KeyboardInterrupt)")
    sys.exit(0)