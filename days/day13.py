from lib import load_input


def solve(data):
    map = set()
    for line in data.split('\n\n')[0].splitlines():
        x, y = line.split(',')
        map.add((int(x), int(y)))
    instructions = data.split('\n\n')[1].splitlines()
    # return part_one(map, instructions)
    return part_two(map, instructions)


def part_one(map, instructions):
    fold(map, instructions[0])
    return len(map)


def fold(map, instruction):
    direction, coord = instruction.split()[2].split('=')
    coord = int(coord)
    remove = set()
    add = set()
    if direction == 'x':
        remove = {(x, y) for x, y in map if x >= coord}
        add = {(coord - (x - coord), y) for x, y in map if x > coord}
    elif direction == 'y':
        remove = {(x, y) for x, y in map if y >= coord}
        add = {(x, coord - (y - coord)) for x, y in map if y > coord}
    map -= remove
    map |= add


def part_two(map, instructions):
    for i, instruction in enumerate(instructions):
        fold(map, instruction)
    xmax, ymax = max(x for x, _ in map), max(y for _, y in map)
    return '\n'.join(''.join('█' if (x, y) in map else ' ' for x in range(xmax + 1)) for y in range(ymax + 1))


if __name__ == '__main__':
    print(solve(load_input('small')))
    print(solve(load_input()))
    print(solve(load_input('large')))
