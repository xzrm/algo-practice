from collections import defaultdict


def evenForest(t_nodes, t_edges, t_from, t_to):
    def build_tree(edges):
        tree = defaultdict(list)
        for start, end in edges:
            tree[start].append(end)
            tree[end].append(start)
        return tree

    nodes = [i + 1 for i in range(t_nodes)]

    stack = []
    seen = set()
    stack.append(nodes[0])
    edges = list(zip(t_from, t_to))
    tree = build_tree(edges)
    parent_child = dict()
    nodes_count = dict()

    while stack:
        parent = stack[-1]
        if parent in seen:
            nodes_count[parent] = 1
            for ch in tree[parent]:
                if parent_child.get(ch, -1) == parent:
                    nodes_count[parent] += nodes_count[ch]
            stack.pop()
        seen.add(parent)
        for ch in tree[parent]:
            if ch not in seen:
                stack.append(ch)
                parent_child[ch] = parent

    edge_counter = 0
    for n1, n2 in edges:
        if nodes_count[n1] % 2 == 0 and (t_nodes - nodes_count[n1]) % 2 == 0:
            print(n1, nodes_count[n1])
            edge_counter += 1

    return edge_counter


input = """
10 9
2 1
3 1
4 3
5 2
6 1
7 2
8 6
9 8
10 8
"""

input_arr = [i.split() for i in input.split("\n") if i]
input_arr.pop(0)
t_from = [int(i[0]) for i in input_arr]
t_to = [int(i[1]) for i in input_arr]
evenForest(len(t_from) + 1, len(t_from), t_from, t_to)
