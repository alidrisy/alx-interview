#!/usr/bin/python3
""" script that reads stdin line by line and computes metrics """
from sys import stdin
import re


status = [200, 301, 400, 401, 403, 404, 405, 500]
i = 0
dict_autput = {}
file_size = 0


def print_all():
    print("File size: {}".format(file_size))
    for k, v in sorted(dict_autput.items()):
        print("{}: {}".format(k, v))


if __name__ == '__main__':
    try:
        for line in stdin:
            i += 1
            try:
                file_size += int(line.split()[-1])
            except Exception:
                pass
            try:
                statu = int(line.split()[-2])
                if statu in dict_autput:
                    dict_autput[statu] += 1
                elif statu in status:
                    dict_autput[statu] = 1
            except Exception:
                pass

            if i % 10 == 0:
                print_all()
    finally:
        print_all()
