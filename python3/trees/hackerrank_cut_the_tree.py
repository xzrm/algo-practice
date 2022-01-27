from collections import defaultdict


def cutTheTree(data, edges):

    node_data = {i + 1: data[i] for i in range(len(data))}
    tree = defaultdict(list)
    for start, end in edges:
        tree[start].append(end)
        tree[end].append(start)

    print(node_data)
    print(tree)

    seen = set()

    def dfs(parent):
        final_sum = 0
        seen.add(parent)
        final_sum += node_data[parent]
        for child in tree[parent]:
            if child not in seen:
                final_sum += dfs(child)

        return final_sum


def def_trees(edges, del_edge):
    edges.remove(del_edge)
    p_1, p_2 = del_edge
    edges_1 = []
    edges_2 = []
    node_ids = [i for i in range(1, len(edges) + 2)]
    edges = [tuple(i) for i in edges]

    def find_edges(edges, parent):
        found_edges = [i for i in edges if i[0] == parent]
        new_edges = list(set(edges) - set(found_edges))
        children = [i[1] for i in found_edges]
        for ch in children:
            found_edges += edges(new_edges, ch)
        return found_edges

    print(find_edges(edges, del_edge[2]))


data = [100, 200, 100, 500, 100, 600]
edges = [[1, 2], [2, 3], [2, 5], [4, 5], [5, 6]]

# cutTheTree(data, edges)
def_trees(edges, [2, 5])
