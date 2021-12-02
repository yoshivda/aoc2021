from lib import load_input


def solve(data):
    # return part_one(data.splitlines())
    return part_two(data.splitlines())


def part_one(data):
    return sum(int(x[1]) for line in data if (x := line.split())[0] == 'forward') \
           * sum(int(x[1]) if x[0] == 'down' else -int(x[1]) for line in data if (x := line.split())[0] != 'forward')


def part_two(data):
    hor = depth = aim = 0
    for line in data:
        dir, num = line.split()
        if dir == 'forward':
            hor += int(num)
            depth += int(num) * aim
        elif dir == 'down':
            aim += int(num)
        elif dir == 'up':
            aim -= int(num)
    return depth * hor


if __name__ == '__main__':
    print(solve(load_input('small')))
    print(solve(load_input()))
