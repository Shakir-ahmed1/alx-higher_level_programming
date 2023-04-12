#!/usr/bin/python3
import sys
""" log parsing module"""
def print_metrics(status_codes, total_size):
    """ prints the metrics according to the given format """
    print("File size: {}".format(total_size))
    for code in sorted(status_codes.keys()):
        if status_codes[code] != 0:
            print("{}: {}".format(code, status_codes[code]))

status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
total_size = 0
count = 0

try:
    for line in sys.stdin:
        count += 1
        split_line = line.split()
        try:
            size = int(split_line[-1])
            total_size += size
        except Exception:
            pass
        try:
            code = int(split_line[-2])
            if code in status_codes:
                status_codes[code] += 1
        except Exception:
            pass

        if count % 10 == 0:
            print_metrics(status_codes, total_size)
except KeyboardInterrupt:
    print_metrics(status_codes, total_size)
    raise
