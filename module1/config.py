"""
JPMC Virtual SEP - InsideSherpa - Module 1
Pedro Teixeira - O734271

Helpers file for configuring AlertService object through cmd line args
This code is factored out so it can be shared between CLI and REST API
"""

import argparse
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

def get_alert_service():
    return AlertService(args.cpu, args.mem, args.disk)