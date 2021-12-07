from lib import load_input


def solve(data):
    # return part_one([int(x) for x in data.split(',')])
    return part_two([int(x) for x in data.split(',')])


def part_one(data):
    return min(sum(abs(x - pos) for x in data) for pos in range(min(data), max(data) + 1))


def part_two(data):
    return min(sum(abs(x - pos) * (abs(x - pos) + 1) // 2 for x in data) for pos in range(min(data), max(data) + 1))


if __name__ == '__main__':
    print(solve(load_input('small')))
    print(solve(load_input()))
