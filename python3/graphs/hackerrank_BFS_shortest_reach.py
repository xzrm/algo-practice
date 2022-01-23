from queue import Queue


def bfs(n, m, edges, s):
    EDGE_WEIGHT = 6
    nodes = {k: set() for k in range(1, n + 1)}
    visited = set()

    for n1, n2 in edges:
        nodes[n1].add(n2)
        nodes[n2].add(n1)

    queue = Queue()

    dists = {k: -1 for k in range(1, n + 1)}
    dists[s] = 0

    queue.put(s)

    visited.add(s)
    while not queue.empty():
        curr_node = queue.get()
        for node in nodes[curr_node]:
            if node not in visited:
                if dists[node] > dists[curr_node] + EDGE_WEIGHT or dists[node] == -1:
                    dists[node] = dists[curr_node] + EDGE_WEIGHT
                queue.put(node)
                visited.add(node)
    dists.pop(s)
    return dists.values()
