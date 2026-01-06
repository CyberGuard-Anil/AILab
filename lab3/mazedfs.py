# Maze representation
maze = [
    ['S', 0, 1, 0],
    [1, 0, 1, 0],
    [0, 0, 0, 'G'],
    [1, 1, 0, 1]
]

def dfs_maze(maze, x, y, visited):
    rows = len(maze)
    cols = len(maze[0])

    # Boundary / wall / visited check
    if (x < 0 or y < 0 or x >= rows or y >= cols or
        maze[x][y] == 1 or (x, y) in visited):
        return False

    # Goal check
    if maze[x][y] == 'G':
        print("Goal found using DFS")
        return True

    visited.add((x, y))

    # Explore all 4 directions
    if (dfs_maze(maze, x+1, y, visited) or
        dfs_maze(maze, x-1, y, visited) or
        dfs_maze(maze, x, y+1, visited) or
        dfs_maze(maze, x, y-1, visited)):
        return True

    return False


# Find Start Position
start_x = start_y = -1
for i in range(len(maze)):
    for j in range(len(maze[0])):
        if maze[i][j] == 'S':
            start_x, start_y = i, j

# ▶ Run DFS
if start_x != -1:
    dfs_maze(maze, start_x, start_y, set())
else:
    print("Start point not found")

