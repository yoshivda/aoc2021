import heapq

from lib import load_input


def adjacent_points(x, xmax, y, ymax):
    return set(filter(lambda p: 0 <= p[0] <= xmax and 0 <= p[1] <= ymax, {(x - 1, y), (x, y - 1), (x + 1, y), (x, y + 1)}))


def solve(data):
    # return part_one([[int(x) for x in line] for line in data.splitlines()])
    return part_two([[int(x) for x in line] for line in data.splitlines()])


def part_one(map):
    pq = [(0, 0, 0)]
    labels = {(0, 0): 0}
    seen = set()
    xmax, ymax = len(map[0]) - 1, len(map) - 1
    while pq:
        risk, x, y = heapq.heappop(pq)
        if (x, y) in seen:
            continue
        if x == xmax and y == ymax:
            return risk
        seen.add((x, y))
        for nx, ny in adjacent_points(x, xmax, y, ymax):
            if (nx, ny) not in seen and ((nx, ny) not in labels or labels[(nx, ny)] > risk + map[ny][nx]):
                labels[(nx, ny)] = risk + map[ny][nx]
                heapq.heappush(pq, (risk + map[ny][nx], nx, ny))


def part_two(map):
    mapdict = {(x, y): map[y][x] for x in range(len(map[0])) for y in range(len(map))}
    pq = [(0, 0, 0)]
    labels = {(0, 0): 0}
    seen = set()
    xmax, ymax = len(map[0]) * 5 - 1, len(map) * 5 - 1
    while pq:
        risk, x, y = heapq.heappop(pq)
        if (x, y) in seen:
            continue
        if x == xmax and y == ymax:
            return risk
        seen.add((x, y))
        for nx, ny in adjacent_points(x, xmax, y, ymax):
            if (nx, ny) not in mapdict:
                xrepeats, yrepeats = nx // len(map[0]), ny // len(map)
                mapdict[(nx, ny)] = ((map[ny % len(map)][nx % len(map[0])] + xrepeats + yrepeats) - 1) % 9 + 1
            if (nx, ny) not in seen and ((nx, ny) not in labels or labels[(nx, ny)] > risk + mapdict[(nx, ny)]):
                labels[(nx, ny)] = risk + mapdict[(nx, ny)]
                heapq.heappush(pq, (risk + mapdict[(nx, ny)], nx, ny))


if __name__ == '__main__':
    print(solve(load_input('small')))
    print(solve(load_input()))
