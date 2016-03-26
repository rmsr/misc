# Uses python3
import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')

def optimal_points(segments):
    # sorted by first, shortest segment
    segments.sort()
    points = []
    start, end = segments.pop(0)
    for seg in segments:
        if end < seg.start:
            points.append(end)
            start, end = seg
            continue
        end = min(end, seg.end)
        start = max(start, seg.start)
    return points + [end]

def main(data):
    # segments must be start < end
    segments = [ Segment(*map(int, line.split())) for line in data ]
    points = optimal_points(segments)
    print(len(points))
    for p in points:
        print(p, end=' ')
    print()

if __name__ == '__main__':
    main(sys.stdin.readlines()[1:])
