#!/usr/bin/python3
# can only run directly if numpy is installed

"""
JPMC Virtual SEP - InsideSherpa - Module 2
Pedro Teixeira - O734271

CLI client for the sanctions package. See README and Jupyter notebook for instructions, or try the --help flag
"""

import argparse
import sys

import sanctions

parser = argparse.ArgumentParser()
parser.add_argument("--list", metavar="-l", type=str, nargs='?',
                    help="the filename of the list of sanctioned names to check against",   default="sanctions.txt", required=False)
parser.add_argument("--basic", "-b", action='store_true',
                    help="if passed in then the basic similarity measure is used instead of the logarithmic one", required=False)
parser.add_argument("--threshold", metavar="-t", type=int, nargs='?',
                    help="minimum similarity score for which to report a hit", default=75, required=False)

args = parser.parse_args()
sim_func = sanctions.basic_similarity if args.basic else sanctions.log_similarity

try:
    while True:
        name = sys.stdin.readline().rstrip()
        if len(name) == 0:
            break
        results = sanctions.screen_name(
            name, args.list, threshold=args.threshold/100, similarity_function=sim_func)
        print('\n'.join(map(lambda x: f"{x[1]} {x[0]}", results)))
except (KeyboardInterrupt):
    print("\nTerminating (KeyboardInterrupt)")
    sys.exit(0)
