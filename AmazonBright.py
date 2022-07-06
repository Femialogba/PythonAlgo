import collections

    # The concept to store an adjacency List is to use a 2d Array , which in python corresponds Nested List
    # Initialize the adjacency matrix
    # Create a matrix with size rows and columns
    #0 edge means I can travel from this node to the other
    # How to return correct paths????
    
def shortestPathBinaryMatrix(grid): 
    if grid[0][0] or grid[-1][-1]:
        return -1
    queue = collections.deque([(0, 0, 1)])
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
    grid [0][0] = 1
    seen = set()
    while queue:
        x, y, path_len = queue.popleft()

        if (x, y) == (len(grid) - 1, len(grid[0]) - 1): 
            seen.add((x,y))
            return [seen , path_len]
        for x_inc, y_inc in directions:
            new_x = x + x_inc 
            new_y = y + y_inc
            

            if (0 <= new_x < len(grid)) and (0 <= new_y < len(grid[0])) and not grid[new_x][new_y]: 
                grid[new_x][new_y] = 1
                queue.append((new_x, new_y, path_len + 1))

    return [None, -1]


grid = []
# Building the grid
grid.append([0,0,0,0,0,0,0,0,0,0])
grid.append([0,0,0,0,0,0,0,0,0,0])
grid.append([0,0,0,0,0,0,0,0,0,0])
grid.append([0,0,0,0,0,0,0,0,0,0])
grid.append([0,0,0,0,0,0,0,0,0,0])
grid.append([0,0,0,0,0,0,0,0,0,0])
grid.append([0,0,0,0,0,0,0,0,0,0]) 
grid.append([0,0,0,0,0,0,1,0,1,1])  # Obstacles are zero (6,7) , (9,7) , (8,7)
grid.append([0,0,0,0,0,0,1,0,0,0])  # (6,8)
grid.append([0,0,0,0,0,0,0,0,0,0])

print(shortestPathBinaryMatrix(grid))




