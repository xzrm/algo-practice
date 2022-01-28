from collections import defaultdict


def cutTheTree(data, edges):
    node_data = {i + 1: data[i] for i in range(len(data))}
    seen = set()
    edges = [tuple(i) for i in edges]

    def dfs(parent, tree):
        final_sum = 0
        seen.add(parent)
        final_sum += node_data[parent]
        for child in tree[parent]:
            if child not in seen:
                final_sum += dfs(child, tree)
        return final_sum

    tree = build_tree(edges)
    tot_sum = dfs(1, tree)
    diff = tot_sum

    for edge in edges:
        p_1, p_2 = edge
        # tree_1, tree_2 = build_trees(edges, [p_1, p_2])
        tree_1 = build_trees(edges, [p_1, p_2])
        seen.clear()
        sum_1 = dfs(p_1, tree_1)
        # seen.clear()
        sum_2 = tot_sum - sum_1
        diff = abs(sum_1 - sum_2) if diff == None else min(diff, abs(sum_1 - sum_2))

    return diff


def build_tree(edges):
    tree = defaultdict(list)
    for start, end in edges:
        tree[start].append(end)
        tree[end].append(start)
    return tree


def build_trees(edges, del_edge):
    edges = [i for i in edges if i != tuple(del_edge)]
    # print(f"{edges=}, {del_edge=}")

    def find_edges(edges, parent):
        found_edges = [i for i in edges if parent in i]
        new_edges = list(set(edges) - set(found_edges))
        new_vals = set([num for i in found_edges for num in i]) - set([parent])
        for ch in new_vals:
            found_edges += find_edges(new_edges, ch)
        return found_edges

    edges_1 = find_edges(edges, del_edge[0])
    # edges_2 = find_edges(edges, del_edge[1])

    return build_tree(edges_1)

    # return build_tree(edges_1), build_tree(edges_2)


data = [100, 200, 100, 500, 100, 600]
edges = [[1, 2], [2, 3], [2, 5], [4, 5], [5, 6]]

cutTheTree(data, edges)
