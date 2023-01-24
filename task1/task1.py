#!/usr/bin/env python3

import sys


def create_array(n):
    for i in range(1, n + 1):
        print(i)


def calculate_way():
    array = [*range(1, n + 1)]
    idx = 0
    _way = ''
    while (idx + n) % len(array) != 0 or len(_way) == 0:
        _way += str(array[idx])
        idx = (idx + m - 1) % len(array)
    return _way


if __name__ == '__main__':
    n = int(sys.argv[1])
    m = int(sys.argv[2])
    way = calculate_way()
    print(way)
