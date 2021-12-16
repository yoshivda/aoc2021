from collections import defaultdict
from functools import cache

from lib import load_input


def solve(data):
    graph = defaultdict(list)
    for line in data.splitlines():
        f, t = line.split('-')
        graph[f].append(t)
        graph[t].append(f)

    # return part_one(graph, 'start', set())
    return part_two(graph, 'start')


def part_one(graph, node, seen):
    if node == 'end':
        return 1
    return sum(part_one(graph, nb, seen | {node}) for nb in graph[node] if nb.isupper() or nb not in seen)


def part_two(graph, node):
    @cache
    def rec_helper(node, seen, duplicate):
        if node == 'end':
            return 1
        new_seen = frozenset(seen | {node}) if node.islower() else seen
        res = sum(rec_helper(nb, new_seen, duplicate) for nb in graph[node] if nb.isupper() or nb not in seen)
        if not duplicate:
            res += sum(rec_helper(nb, new_seen, True) for nb in graph[node] if nb.islower() and nb not in ('start', 'end') and nb in seen)
        return res
    return rec_helper(node, frozenset(), False)


if __name__ == '__main__':
    print(solve(load_input('small')))
    print(solve(load_input('medium')))
    print(solve(load_input('large')))
    print(solve(load_input()))
