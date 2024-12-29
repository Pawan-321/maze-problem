def solve_maze(maze):
    """
    Solves a maze using DFS algorithm.
    The maze is represented as a 2D list where:
    - 0 represents a path
    - 1 represents a wall
    - 'S' represents the start point
    - 'E' represents the end point
    Returns the path from start to end if found, None otherwise.
    """
    if not maze or not maze[0]:
        return None
    
    rows, cols = len(maze), len(maze[0])
    # Find start and end positions
    start = None
    end = None
    for i in range(rows):
        for j in range(cols):
            if maze[i][j] == 'S':
                start = (i, j)
            elif maze[i][j] == 'E':
                end = (i, j)
    
    if not start or not end:
        return None
    
    def is_valid(x, y):
        return (0 <= x < rows and 
                0 <= y < cols and 
                (maze[x][y] == 0 or maze[x][y] == 'E'))
    
    def dfs(x, y, visited, path):
        if (x, y) == end:
            return path
        
        # Possible moves: right, down, left, up
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        for dx, dy in directions:
            next_x, next_y = x + dx, y + dy
            if (is_valid(next_x, next_y) and 
                (next_x, next_y) not in visited):
                visited.add((next_x, next_y))
                next_path = dfs(next_x, next_y, visited, path + [(next_x, next_y)])
                if next_path:
                    return next_path
                visited.remove((next_x, next_y))
        
        return None
    
    # Start DFS from the start position
    visited = {start}
    path = dfs(start[0], start[1], visited, [start])
    
    return path

# Example usage and test
def print_solution(maze, path):
    """
    Prints the maze with the solution path marked with '*'
    """
    if not path:
        print("No solution found!")
        return
    
    solution = [['#' if cell == 1 else ' ' for cell in row] for row in maze]
    for x, y in path:
        if maze[x][y] not in ['S', 'E']:
            solution[x][y] = '*'
    
    for row in solution:
        print(' '.join(map(str, row)))

# Test the implementation
test_maze = [
    ['S', 0, 0, 1, 0],
    [1, 1, 0, 1, 0],
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 1, 'E']
]

print("Original Maze:")
for row in test_maze:
    print(' '.join(map(str, row)))

print("\nSolution:")
path = solve_maze(test_maze)
print_solution(test_maze, path)
