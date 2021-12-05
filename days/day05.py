import re
from collections import defaultdict

from lib import load_input


def solve(data):
    # return part_one(data.splitlines())
    return part_two(data.splitlines())


def part_one(data):
    hits = defaultdict(int)
    lines = [tuple(int(x) for x in re.split(',| -> ', line)) for line in data]
    for line in lines:
        x1, y1, x2, y2 = line
        if x1 == x2:
            for y in range(min(y1, y2), max(y1, y2) + 1):
                hits[(x1, y)] += 1
        elif y1 == y2:
            for x in range(min(x1, x2), max(x1, x2) + 1):
                hits[(x, y1)] += 1
    return sum(v > 1 for v in hits.values())


def part_two(data):
    hits = defaultdict(int)
    lines = [tuple(int(x) for x in re.split(',| -> ', line)) for line in data]
    for line in lines:
        x1, y1, x2, y2 = line
        if x1 == x2:
            for y in range(min(y1, y2), max(y1, y2) + 1):
                hits[(x1, y)] += 1
        elif y1 == y2:
            for x in range(min(x1, x2), max(x1, x2) + 1):
                hits[(x, y1)] += 1
        else:
            dx = 1 if x2 > x1 else -1
            dy = 1 if y2 > y1 else -1
            y = y1
            for x in range(x1, x2 + dx, dx):
                hits[(x, y)] += 1
                y += dy
    return sum(v > 1 for v in hits.values())


if __name__ == '__main__':
    print(solve(load_input('small')))
    print(solve(load_input()))
