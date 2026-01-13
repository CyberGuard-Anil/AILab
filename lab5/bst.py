import heapq

def manhattan(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def best_first_search(start, goal, rows, cols):
    visited = set()
    pq = []
    heapq.heappush(pq, (manhattan(start, goal), start))

    while pq:
        _, current = heapq.heappop(pq)

        if current in visited:
            continue

        visited.add(current)
        print(current)

        if current == goal:
            print("Treasure Found")
            return

        x, y = current
        for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols:
                if (nx, ny) not in visited:
                    heapq.heappush(pq, (manhattan((nx, ny), goal), (nx, ny)))

    print("Treasure Not Found")

if __name__ == "__main__":
    rows = 4
    cols = 4
    start = (0, 0)
    goal = (3, 3)
    best_first_search(start, goal, rows, cols)

