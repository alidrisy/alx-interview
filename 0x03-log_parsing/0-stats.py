#!/usr/bin/python3
""" script that reads stdin line by line and computes metrics """
from sys import stdin
import re


if __name__ == '__main__':
    patern = re.compile(
            r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3} - \[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}.\d+\] "GET /projects/260 HTTP/1.1" (.{3}) (\d+)')  # nopep8
    status = ["200", "301", "400", "401", "403", "404", "405", "500"]
    i = 0
    dict_autput = {}
    file_size = 0
    try:
        for line in stdin:
            line = line.strip()
            if (patern.fullmatch(line)):
                file_size += int(line.split()[-1])
                statu = line.split()[-2]
                if statu in dict_autput:
                    dict_autput[statu] += 1
                elif statu.isdigit() and statu in status:
                    dict_autput[statu] = 1
                i += 1
                if i % 10 == 0:
                    print("File size: {}".format(file_size))
                    for k, v in sorted(dict_autput.items()):
                        print("{}: {}".format(k, v))
    finally:
        print("File size: {}".format(file_size))
        for k, v in sorted(dict_autput.items()):
            print("{}: {}".format(k, v))
