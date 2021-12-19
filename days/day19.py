import itertools
from functools import cache

from lib import load_input


rotations = [
        lambda x, y, z: (x, y, z),
        lambda x, y, z: (x, -z, y),
        lambda x, y, z: (x, -y, -z),
        lambda x, y, z: (x, z, -y),
        lambda x, y, z: (y, z, x),
        lambda x, y, z: (y, -x, z),
        lambda x, y, z: (y, -z, -x),
        lambda x, y, z: (y, x, -z),
        lambda x, y, z: (z, x, y),
        lambda x, y, z: (z, -y, x),
        lambda x, y, z: (z, -x, -y),
        lambda x, y, z: (z, y, -x),
        lambda x, y, z: (-z, -y, -x),
        lambda x, y, z: (-z, x, -y),
        lambda x, y, z: (-z, y, x),
        lambda x, y, z: (-z, -x, y),
        lambda x, y, z: (-y, -x, -z),
        lambda x, y, z: (-y, z, -x),
        lambda x, y, z: (-y, x, z),
        lambda x, y, z: (-y, -z, x),
        lambda x, y, z: (-x, -z, -y),
        lambda x, y, z: (-x, y, -z),
        lambda x, y, z: (-x, z, y),
        lambda x, y, z: (-x, -y, z),
    ]


def solve(data):
    # return part_one(data.split('\n\n'))
    return part_two(data.split('\n\n'))


def distance(p1, p2):
    xa, ya, za = p1
    xb, yb, zb = p2
    return abs(xa - xb) + abs(ya - yb) + abs(za - zb)


@cache  # why make efficient code when python can optimise it for you :)
def distances(points):
    return {distance(p1, p2): (p1, p2) for p1, p2 in itertools.combinations(points, 2)}


def try_align(scanner, intersect, known_points, known_distances):
    for i_dist in intersect:
        k1, k2 = known_distances[i_dist]
        n1, n2 = distances(scanner)[i_dist]
        for rot in rotations:
            rn1 = rot(*n1)
            rn2 = rot(*n2)
            if distance(k1, rn1) == distance(k2, rn2):
                dx, dy, dz = (k1[i] - rn1[i] for i in range(3))
            elif distance(k1, rn2) == distance(k2, rn1):
                dx, dy, dz = (k1[i] - rn2[i] for i in range(3))
            else:
                continue
            rot_points = {rot(*p) for p in scanner}
            trans_points = {(x + dx, y + dy, z + dz) for x, y, z in rot_points}
            if len(trans_points.intersection(known_points)) >= 12:
                return trans_points, (dx, dy, dz)
    return None, None


def align_map(data):
    scanners = [frozenset(tuple(map(int, line.split(','))) for line in part.splitlines()[1:]) for part in data]
    scanner_pos = {0: (0, 0, 0)}
    known_points = scanners[0]
    known_distances = distances(known_points)
    while len(scanner_pos.keys()) < len(scanners):
        for i in (set(range(len(scanners))) - scanner_pos.keys()):
            if intersect := set(distances(scanners[i]).keys()).intersection(known_distances.keys()):
                a, b = try_align(scanners[i], intersect, known_points, known_distances)
                if a:
                    known_points = frozenset(known_points | a)
                    known_distances = distances(known_points)
                    scanner_pos[i] = b
    return known_points, scanner_pos


def part_one(data):
    points, _ = align_map(data)
    return len(points)


def part_two(data):
    _, scanner_pos = align_map(data)
    return max(distance(p1, p2) for p1, p2 in itertools.combinations(scanner_pos.values(), 2))


if __name__ == '__main__':
    print(solve(load_input('small')))
    print(solve(load_input()))
