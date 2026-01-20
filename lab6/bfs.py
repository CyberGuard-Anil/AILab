from collections import deque

def bfs(graph, start, goal):
    queue = deque()
    queue.append((start, [start]))
    visited = set()

    while queue:
        node, path = queue.popleft()

        if node == goal:
            return path

        if node not in visited:
            visited.add(node)

            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append((neighbor, path + [neighbor]))

    return None


graph = {
    'A': ['B', 'C'],
    'B': ['C', 'D'],
    'C': ['D'],
    'D': []
}

start = 'A'
goal = 'D'

path = bfs(graph, start, goal)

print("BFS Path:", path)
print("Number of Steps:", len(path) - 1)

