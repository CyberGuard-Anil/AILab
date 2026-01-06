graph = {
    'A': [('B', 1), ('D', 2)],
    'B': [('A', 1), ('C', 2), ('E', 2)],
    'C': [('B', 2), ('F', 3)],
    'D': [('A', 2), ('E', 1)],
    'E': [('D', 1), ('B', 2), ('F', 1)],
    'F': [('C', 3), ('E', 1)]
}
import heapq
def uniform_cost_search(graph, start, goal):
    pq = []
    heapq.heappush(pq, (0, start, [start]))  
    visited = set()

    while pq:
        cost, node, path = heapq.heappop(pq)

        if node in visited:
            continue
        visited.add(node)

        if node == goal:
            return cost, path

        for neighbour, edge_cost in graph[node]:
            if neighbour not in visited:
                heapq.heappush(
                    pq,
                    (cost + edge_cost, neighbour, path + [neighbour])
                )

    return None
result = uniform_cost_search(graph, 'A', 'F')

if result:
    cost, path = result
    print("Path:", " -> ".join(path))
    print("Total Cost:", cost)
else:
    print("Path Not Found")

