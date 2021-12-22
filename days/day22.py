import re

from lib import load_input


def solve(data):
    parsed = [(line[1] == 'n', *list(map(int, re.findall(r'-?\d+', line)))) for line in data.splitlines()]
    # return part_one(parsed)
    return part_two(parsed)


def part_one(cubes):
    return calculate(cubes, True)


def part_two(cubes):
    return calculate(cubes, False)


def calculate(cubes, limit):
    processed = []
    for cur in cubes:
        on, xmin, xmax, ymin, ymax, zmin, zmax = cur
        if limit and (min(xmin, ymin, zmin) < -50 or max(xmax, ymax, zmax) > 50):
            continue
        processed.extend([(not pc[0], *ol) for pc in processed if (ol := overlap(cur, pc))])
        if on:
            processed.append(cur)
    return sum(volume(*c[1:]) * (1 if c[0] else -1) for c in processed)


def volume(xmin, xmax, ymin, ymax, zmin, zmax):
    return abs(xmax-xmin + 1) * abs(ymax-ymin + 1) * abs(zmax-zmin + 1)


def overlap(c1, c2):
    _, xmin1, xmax1, ymin1, ymax1, zmin1, zmax1 = c1
    _, xmin2, xmax2, ymin2, ymax2, zmin2, zmax2 = c2
    if xmax1 < xmin2 or xmax2 < xmin1 or ymax1 < ymin2 or ymax2 < ymin1 or zmax1 < zmin2 or zmax2 < zmin1:
        return 0
    return max(xmin1, xmin2), min(xmax1, xmax2), max(ymin1, ymin2), min(ymax1, ymax2), max(zmin1, zmin2), min(zmax1, zmax2)


if __name__ == '__main__':
    print(solve(load_input('small')))
    print(solve(load_input('middle')))
    print(solve(load_input()))
