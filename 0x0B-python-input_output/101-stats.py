#!/usr/bin/python3
"""
Write a script that reads stdin line by line and computes metrics:
"""
import sys
import re
result = []
file_size = []
counter = 0
dc = {"200": 0, "301": 0, "400": 0, "401": 0,
      "403": 0, "404": 0, "405": 0, "500": 0}
try:
    for line in sys.stdin:
        match = re.match(r'^(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - \[(.*)\]'
                         r' "GET \/projects\/260 HTTP\/1\.1" (\d{3}) (\d+)',
                         line)
        result.append(match.group(3))
        if match.group(3) in dc:
            dc[match.group(3)] += 1
        file_size.append(int(match.group(4)))
        counter += 1
        if counter % 10 == 0:
            print(f"File size: {sum(file_size[:counter+10])}")
            for d in sorted(dc):
                if dc[d] != 0:
                    print(f"{d}: {dc[d]}")
except KeyboardInterrupt:
    pass
finally:
    print(f"File size: {sum(file_size)}")
    for d in sorted(dc):
        if dc[d] != 0:
            print(f"{d}: {dc[d]}")
