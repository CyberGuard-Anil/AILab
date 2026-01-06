# Graph representation
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

def dfs(graph, node, visited=None):
    if visited is None:
        visited = set()        # Visited set create

    print(node, end=" ")       # Current node print
    visited.add(node)          # Node ko visited mark

    # Neighbours ko recursively visit karo
    for neighbour in graph[node]:
        if neighbour not in visited:
            dfs(graph, neighbour, visited)

# Function call
print("DFS Traversal:", end=" ")
dfs(graph, 'A')

