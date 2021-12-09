import numpy as np

from lib import load_input


def solve(data):
    map = [[int(x) for x in line] for line in data.splitlines()]
    # return part_one(map)
    return part_two(map)


def adjacent_points(x, xmax, y, ymax):
    return set(filter(lambda p: 0 <= p[0] <= xmax and 0 <= p[1] <= ymax, {(x - 1, y), (x, y - 1), (x + 1, y), (x, y + 1)}))


def low_points(map):
    xmax, ymax = len(map[0]) - 1, len(map) - 1
    return {(x, y) for x in range(len(map[0])) for y in range(len(map))
            if (adjacent := adjacent_points(x, xmax, y, ymax)) and all(map[py][px] > map[y][x]for px, py in adjacent)}


def part_one(map):
    return sum(map[y][x] + 1 for x, y in low_points(map))


def part_two(map):
    return np.prod([len(x) for x in sorted([({(x, y)} | higher_neighbours({(x, y)}, map)) for x, y in low_points(map)],
                                           key=len, reverse=True)[:3]])


def higher_neighbours(points, map):
    res = {(px, py) for x, y in points for px, py in adjacent_points(x, len(map[0]) - 1, y, len(map[0]) - 1) if map[y][x] < map[py][px] < 9}
    if not res:
        return set()
    return res | higher_neighbours(res, map)


if __name__ == '__main__':
    print(solve(load_input('small')))
    print(solve(load_input()))
