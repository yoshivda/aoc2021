from lib import load_input


def solve(data):
    # return part_one(list(map(int, data.split(','))))
    return part_two(list(map(int, data.split(','))))


def part_one(fish):
    for _ in range(80):
        for i in range(len(fish)):
            if fish[i] == 0:
                fish[i] = 6
                fish.append(8)
            else:
                fish[i] -= 1
    return len(fish)


def part_two(data):
    increases = [0] * 9
    fish = len(data)
    for f in data:
        increases[f] += 1

    for day in range(256):
        fish += increases[day % 9]
        increases[(day - 2) % 9] += increases[day % 9]
    return fish


if __name__ == '__main__':
    print(solve(load_input('small')))
    print(solve(load_input()))
