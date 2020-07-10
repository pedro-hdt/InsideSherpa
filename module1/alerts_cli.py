#!/usr/bin/python3

"""
JPMC Virtual SEP - InsideSherpa - Module 1
Pedro Teixeira - O734271

CLI client for the alerts package. See README for instructions, or try the 
--help flag
"""

import argparse
import config
import sys

from alerts import AlertService

alert_service = config.get_alert_service()

try:
    while True:
        line = sys.stdin.readline().rstrip()
        if len(line) == 0:
            break
        print(alert_service.alert_me(line))
except (EOFError, KeyboardInterrupt):
    print("\nTerminating (EOF / KeyboardInterrupt)")
    sys.exit(0)