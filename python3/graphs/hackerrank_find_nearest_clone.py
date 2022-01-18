from queue import Queue
import itertools


def findShortest(graph_nodes, graph_from, graph_to, ids, val):
    graph = {k: [] for k in range(1, graph_nodes + 1)}
    colors = {i + 1: ids[i] for i in range(len(ids))}

    for i, j in zip(graph_from, graph_to):
        graph[i].append(j)
        graph[j].append(i)

    searched_ids = [i for i, j in colors.items() if j == val]
    combi = itertools.combinations(searched_ids, 2)
    min_dist = -1

    for src, end in combi:
        Q = Queue()
        distance = {k: 9999999 for k in graph.keys()}
        visited_vertices = set()

        Q.put(src)
        visited_vertices.update({src})
        found = False
        while not Q.empty() and not found:
            vertex = Q.get()
            if vertex == src:
                distance[vertex] = 0
            for nb in graph[vertex]:
                if nb not in visited_vertices:
                    if distance[nb] > distance[vertex] + 1:
                        distance[nb] = distance[vertex] + 1
                    if nb == end:
                        found = True
                        break
                    Q.put(nb)
                    visited_vertices.update({nb})

        if min_dist == -1:
            min_dist = distance[end]
        else:
            min_dist = min(min_dist, distance[end])
    return min_dist


print("Least distance of vertices from vertex 0 is:")
print(findShortest(6, [1, 1, 2, 3, 3], [2, 3, 4, 5, 6], [1, 2, 3, 3, 2, 2], 2))
