from collections import defaultdict

from lib import load_input


def solve(data):
    graph = defaultdict(list)
    for line in data.splitlines():
        f, t = line.split('-')
        graph[f].append(t)
        graph[t].append(f)

    # return part_one(graph, 'start', [])
    return part_two(graph, 'start', [])


def part_one(graph, node, path):
    if node == 'end':
        return 1
    return sum(part_one(graph, nb, path + [node]) for nb in graph[node] if nb.isupper() or nb not in path)


def part_two(graph, node, path):
    if node == 'end':
        return 1
    cur_path = path + [node]
    return sum(part_two(graph, nb, cur_path) for nb in graph[node] if nb.isupper() or nb not in path or
               (all(cur_path.count(n) == 1 for n in cur_path if n.islower()) and nb not in ('start', 'end')))


if __name__ == '__main__':
    print(solve(load_input('small')))
    print(solve(load_input('medium')))
    print(solve(load_input('large')))
    print(solve(load_input()))
