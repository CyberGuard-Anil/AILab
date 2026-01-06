graph = {
	'A' : ['B', 'D'],
	'B' : ['A', 'C', 'E'],
	'C' : ['B', 'F'],
	'D' : ['A', 'E'],
	'E' : ['D', 'B', 'F'],
	'F' : ['C', 'E']
}

def build_path(visit1, visit2, meet):
    path1 = []
    node = meet

    while node is not None:
        path1.append(node)
        node = visit1[node]

    path1.reverse()

    path2 = []
    node = visit2[meet]

    while node is not None:
        path2.append(node)
        node = visit2[node]

    return path1 + path2

from collections import deque

def bidirectional_bfs(graph, start, goal):
    q1 = deque([start])
    q2 = deque([goal])

    visit1 = {start: None}
    visit2 = {goal: None}

    while q1 and q2:
        # Start side
        current1 = q1.popleft()
        for n in graph[current1]:
            if n not in visit1:
                visit1[n] = current1
                q1.append(n)
                if n in visit2:
                    return build_path(visit1, visit2, n)

        # Goal side
        current2 = q2.popleft()
        for n in graph[current2]:
            if n not in visit2:
                visit2[n] = current2
                q2.append(n)
                if n in visit1:
                    return build_path(visit1, visit2, n)

    return None

path = bidirectional_bfs(graph, 'A', 'F')

if path:
    print("Path:", " -> ".join(path))
else:
    print("Path Not Found")


