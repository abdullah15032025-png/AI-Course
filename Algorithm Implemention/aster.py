import heapq

def astar(grid, start, end):
    open_set = [(0, start)]
    came_from = {}
    g_score = {start: 0}
    
    while open_set:
        _, current = heapq.heappop(open_set)
        if current == end:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            return path[::-1]
        
        for dx, dy in [(0,1),(1,0),(0,-1),(-1,0)]:
            neighbor = (current[0] + dx, current[1] + dy)
            if 0 <= neighbor[0] < len(grid) and 0 <= neighbor[1] < len(grid[0]) and grid[neighbor[0]][neighbor[1]] == 0:
                new_g = g_score[current] + 1
                if neighbor not in g_score or new_g < g_score[neighbor]:
                    g_score[neighbor] = new_g
                    f_score = new_g + abs(neighbor[0] - end[0]) + abs(neighbor[1] - end[1])
                    heapq.heappush(open_set, (f_score, neighbor))
                    came_from[neighbor] = current
    return None

# User input
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))
grid = [[int(cell) for cell in input(f"Row {r} (0 for empty, 1 for obstacle): ").split()] for r in range(rows)]
start = tuple(map(int, input("Start (row col): ").split()))
end = tuple(map(int, input("End (row col): ").split()))

# Find path
path = astar(grid, start, end)
print("Path:", path if path else "No path found")