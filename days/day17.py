import re

from lib import load_input


def solve(data):
    # return part_one(*list(map(int, re.findall(r'-?\d+', data))))
    return part_two(*list(map(int, re.findall(r'-?\d+', data))))


def part_one(xmin, xmax, ymin, ymax):
    xpos = 0
    for i in range(1, xmax // 4):
        xpos += i
        if xmin <= xpos <= xmax:
            dx = i
            break
    found = False
    dy = 1
    while True:
        reaches = reaches_square(dx, dy, xmin, xmax, ymin, ymax)
        if found and not reaches:
            break
        found = reaches
        dy += 1
    return dy * (dy - 1) // 2


def reaches_square(dx, dy, xmin, xmax, ymin, ymax):
    x = y = 0
    while x <= xmax:
        x += dx
        y += dy
        if xmin <= x <= xmax and ymin <= y <= ymax:
            return True
        if y < ymin and dy < 0 or ((x < xmin or x > xmax) and dx == 0):
            return False
        if dx > 0:
            dx -= 1
        elif dx < 0:
            dx += 1
        dy -= 1
    return False


def part_two(xmin, xmax, ymin, ymax):
    return len({(dx, dy) for dx in range(1, xmax + 1) for dy in range(ymin, 140) if reaches_square(dx, dy, xmin, xmax, ymin, ymax)})


if __name__ == '__main__':
    print(solve(load_input('small')))
    print(solve(load_input()))
