from lib import load_input


def solve(data):
    # return part_one(*data.split('\n\n'))
    return part_two(*data.split('\n\n'))


def part_one(algo, grid):
    return compute(algo, grid, 2)


def part_two(algo, grid):
    return compute(algo, grid, 50)


def compute(algo, grid, repeats):
    grid = grid.splitlines()
    coords = {(x, y) for x in range(len(grid[0])) for y in range(len(grid)) if grid[y][x] == '#'}
    switching = algo[0] == '#'
    store_light_chars = False
    for _ in range(repeats):
        coords = enhance(coords, algo, switching, store_light_chars)
        store_light_chars = not store_light_chars
    return len(coords)


def enhance(coords, algo, switching, store_light_chars):
    res = set()
    xmin, xmax = min(x for x, _ in coords), max(x for x, _ in coords)
    ymin, ymax = min(y for _, y in coords), max(y for _, y in coords)
    for y in range(ymin - 2, ymax + 1):
        for x in range(xmin - 2, xmax + 1):
            if not switching or not store_light_chars:
                bitstr = ''.join('1' if (mx, my) in coords else '0' for my in range(y, y + 3) for mx in range(x, x + 3))
            else:
                bitstr = ''.join('0' if (mx, my) in coords else '1' for my in range(y, y + 3) for mx in range(x, x + 3))
            store_char = '#' if not switching or store_light_chars else '.'
            if algo[int(bitstr, 2)] == store_char:
                res.add((x + 1, y + 1))
    return res


if __name__ == '__main__':
    print(solve(load_input('small')))
    print(solve(load_input()))
