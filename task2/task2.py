#!/usr/bin/env python3

import sys


class Circle:
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def read_circle(file):
    circle_file = open(file, 'r')
    coordinates = circle_file.readline().split(' ')
    a_circle = Circle(float(coordinates[0]), float(coordinates[1]), float(circle_file.readline()))
    circle_file.close()
    return a_circle


def read_points(file):
    points_list = []
    points_file = open(file, 'r')
    for line in points_file.readlines():
        split_line = line.split(' ')
        points_list.append(Point(float(split_line[0]), float(split_line[1])))
    points_file.close()
    return points_list


def is_point_in_circle(point, circle):
    value = ((point.x - circle.x) ** 2 + (point.y - circle.y) ** 2) - circle.r ** 2
    if value == 0:
        return 0
    elif value < 0:
        return 1
    else:
        return 2


if __name__ == '__main__':
    _circle = read_circle(sys.argv[1])
    _points = read_points(sys.argv[2])
    for _point in _points:
        print(is_point_in_circle(_point, _circle))
