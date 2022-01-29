from collections import defaultdict


def cutTheTree(data, edges):
    def build_tree(edges):
        tree = defaultdict(list)
        for start, end in edges:
            tree[start].append(end)
            tree[end].append(start)
        return tree

    nodes = [i + 1 for i in range(len(data))]
    tot_sum = sum(data)
    seen = set()
    stack = []
    stack.append(nodes[0])
    tree = build_tree(edges)
    parent_child = dict()
    nodes_weight = dict()
    min_diff = None

    while stack:
        parent = stack[-1]

        if parent in seen:
            nodes_weight[parent] = data[parent - 1]
            for ch in tree[parent]:
                if parent_child.get(ch, -1) == parent:
                    nodes_weight[parent] += nodes_weight[ch]

            sum_1 = nodes_weight[parent]
            sum_2 = tot_sum - sum_1
            min_diff = (
                abs(sum_1 - sum_2)
                if min_diff == None
                else min(min_diff, abs(sum_1 - sum_2))
            )

            stack.pop()
        seen.add(parent)
        for ch in tree[parent]:
            if ch not in seen:
                stack.append(ch)
                parent_child[ch] = parent

    return min_diff


data = [100, 200, 100, 500, 100, 600]
edges = [[1, 2], [2, 3], [2, 5], [4, 5], [5, 6]]
# data = [100, 200, 100, 500]
# edges = [[1, 2], [2, 3], [2, 4]]

cutTheTree(data, edges)
