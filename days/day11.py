from lib import load_input


def solve(data):
    map = [[int(x) for x in line] for line in data.splitlines()]
    # return part_one(map)
    return part_two(map)


def neighbours(x, y, map):
    xmax, ymax = len(map[0]) - 1, len(map) - 1
    return set(filter(lambda p: 0 <= p[0] <= xmax and 0 <= p[1] <= ymax and (p[0] != x or p[1] != y),
                      {(x + i, y + j) for i in range(-1, 2) for j in range(-1, 2)}))


def increase_all(map):
    res = 0
    for y in range(len(map)):
        for x in range(len(map[0])):
            map[y][x] += 1
            if map[y][x] == 10:
                res += flash(map, x, y)
    for y in range(len(map)):
        for x in range(len(map[0])):
            if map[y][x] >= 10:
                map[y][x] = 0
    return res


def flash(map, x, y):
    res = 1
    for nx, ny in neighbours(x, y, map):
        map[ny][nx] += 1
        if map[ny][nx] == 10:
            res += flash(map, nx, ny)
    return res


def part_one(map):
    return sum(increase_all(map) for _ in range(100))


def part_two(map):
    size = len(map) * len(map[0])
    step = 1
    while increase_all(map) != size:
        step += 1
    return step


if __name__ == '__main__':
    print(solve(load_input('small')))
    print(solve(load_input()))
