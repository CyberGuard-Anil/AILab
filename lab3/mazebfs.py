from collections import deque

def bfs_maze(maze):
    rows, cols = len(maze), len(maze[0])
    visited = set()
    queue = deque()

    # Start position find karo
    for i in range(rows):
        for j in range(cols):
            if maze[i][j] == 'S':
                queue.append((i, j))
                visited.add((i, j))

    directions = [(-1,0), (1,0), (0,-1), (0,1)]  # U D L R

    while queue:
        x, y = queue.popleft()

        # Goal check
        if maze[x][y] == 'G':
            print("Goal found using BFS")
            return True

        # Neighbours explore karo
        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if (0 <= nx < rows and 0 <= ny < cols and
                maze[nx][ny] != 1 and
                (nx, ny) not in visited):

                queue.append((nx, ny))
                visited.add((nx, ny))

    print("Goal not found using BFS")
    return False


# Maze input
maze = [
    ['S', 0, 1, 0],
    [1, 0, 1, 0],
    [0, 0, 0, 'G'],
    [1, 1, 0, 1]
]

bfs_maze(maze)

