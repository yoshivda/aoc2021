from lib import load_input


def solve(data):
    lines = data.splitlines()
    xmax, ymax = len(lines[0]), len(lines)
    east = {(x, y) for x in range(xmax) for y in range(ymax) if lines[y][x] == '>'}
    south = {(x, y) for x in range(xmax) for y in range(ymax) if lines[y][x] == 'v'}
    return part_one(east, south, xmax, ymax)


def part_one(east, south, xmax, ymax):
    something_moved = True
    steps = 0
    while something_moved:
        steps += 1
        something_moved = False

        moving_east = {(x, y) for x, y in east if ((x + 1) % xmax, y) not in south and ((x + 1) % xmax, y) not in east}
        something_moved |= bool(moving_east)
        east -= moving_east
        east |= {((x + 1) % xmax, y) for x, y in moving_east}

        moving_south = {(x, y) for x, y in south if (x, (y + 1) % ymax) not in south and (x, (y + 1) % ymax) not in east}
        something_moved |= bool(moving_south)
        south -= moving_south
        south |= {(x, (y + 1) % ymax) for x, y in moving_south}
    return steps


if __name__ == '__main__':
    # print(solve(load_input('line')))
    # print(solve(load_input('wrap')))
    print(solve(load_input('small')))
    print(solve(load_input()))
