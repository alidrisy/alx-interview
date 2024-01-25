#!/usr/bin/python3
""" script that reads stdin line by line and computes metrics """
from sys import stdin
import re


pattern = r"^\d+\.\d+\.\d+\.\d+ - \[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d+\] \"GET /projects/260 HTTP/1\.1\" \d+ \d+$"  # nopep8


if __name__ == '__main__':
    status = ["200", "301", "400", "401", "403", "404", "405", "500"]
    i = 0
    dict_autput = {}
    file_size = 0
    try:
        for line in stdin:
            patern = re.compile(pattern)
            if bool(patern.match(line)):
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
