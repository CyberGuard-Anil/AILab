import heapq

def uniform_cost_search(graph, start, goal):
    pq = []
    heapq.heappush(pq, (0, start, [start]))
    visited = set()

    while pq:
        cost, node, path = heapq.heappop(pq)

        if node == goal:
            return path, cost

        if node not in visited:
            visited.add(node)

            for neighbor, weight in graph[node]:
                if neighbor not in visited:
                    heapq.heappush(
                        pq,
                        (cost + weight, neighbor, path + [neighbor])
                    )

    return None, float('inf')


# -------- MAIN --------
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('C', 2), ('D', 5)],
    'C': [('D', 1)],
    'D': []
}

start = 'A'
goal = 'D'

path, cost = uniform_cost_search(graph, start, goal)

print("Optimal Path:", path)
print("Total Cost:", cost)

