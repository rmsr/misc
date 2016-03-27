#!/bin/python3
from collections import namedtuple

"""
Given a set of line segments and points, determine how many segs overlap each
point.

naive is n^2.

fast_count is nlogn. Build a sorted list of starts, stops, points, do a scan
keeping a running count of segments, emit counts for each point found.

A fancier implementation might use interval or segment trees, but might not be
any faster. More useful for streaming segments or points, though.
"""

Point = namedtuple('Point','loc type order')

def fast_count_segments(segments, points):
    # order type by start, point, stop for accurate overlap counting. preserve
    # point ordering for correct output
    START = 1
    STOP = 3
    POINT = 2

    line = []
    for start, stop in segments:
        line.append(Point(start, START, None))
        line.append(Point(stop, STOP, None))
    for index, point in enumerate(points):
        line.append(Point(point, POINT, index))
    line.sort()
    segs = 0
    counts = [0] * len(points)
    for _, ptype, order in line:
        if ptype == START:
            segs += 1
        elif ptype == STOP:
            segs -= 1
        else:
            counts[order] = segs
    return counts

def naive_count_segments(segments, points):
    return ( sum(1 for s, e in segments if s < p < e) for p in points )

count_segments = fast_count_segments

def main():
    segments = [ [ int(i) for i in input().split() ]
                    for _ in range( int( input().split()[0] ) ) ]
    points = [ int(i) for i in input().split() ]
    print(*count_segments(segments, points))

if __name__ == '__main__':
    main()
