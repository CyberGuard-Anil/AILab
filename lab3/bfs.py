from collections import deque   # Queue ke liye

# Graph representation using dictionary
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

def bfs(graph, start):
    visited = set()            # Visited nodes ko track karne ke liye
    queue = deque()            # Queue create ki
    queue.append(start)        # Start node queue mein daala

    print("BFS Traversal:", end=" ")

    while queue:
        node = queue.popleft()   # Queue se element nikala

        if node not in visited:
            print(node, end=" ") # Node print kiya
            visited.add(node)    # Node ko visited mark kiya

            # Neighbours ko queue mein daalo
            for neighbour in graph[node]:
                if neighbour not in visited:
                    queue.append(neighbour)

# Function call
bfs(graph, 'A')

