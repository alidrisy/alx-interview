#!/usr/bin/python3
""" script that reads stdin line by line and computes metrics """
from sys import stdin
import re

pattern =\
    r"^(?P<ip_addrees>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - \[(?P<date>.*?)\] "
r"\"GET /projects/260 HTTP/1.1\" "
r"(?P<status_code>\d{3}) (?P<file_size>\d+)$"


i = 0
dict_autput = {}
file_size = 0
try:
    for line in stdin:
        match = re.match(pattern, line)
        if match:
            file_size += int(line.split()[-1])
            status = line.split()[-2]
            if status in dict_autput:
                dict_autput[status] += 1
            else:
                dict_autput[status] = 1
            i += 1
        if i % 10 == 0:
            print(f"File size: {file_size}")
            for k, v in sorted(dict_autput.items()):
                print(f"{k}: {v}")
except KeyboardInterrupt:
    print(f"File size: {file_size}")
    for k, v in sorted(dict_autput.items()):
        print(f"{k}: {v}")
