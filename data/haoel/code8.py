def in_bounds(grid, i, j):
    return 0 <= i < len(grid) and 0 <= j < len(grid[0])

def is_land(grid, i, j):
    return in_bounds(grid, i, j) and grid[i][j] == '1'

def sink(grid, i, j):
    if not is_land(grid, i, j):
        return
    grid[i][j] = '0'
    for di, dj in [(1,0),(-1,0),(0,1),(0,-1)]:
        sink(grid, i + di, j + dj)

def count_islands(grid):
    return sum(
        1 for i in range(len(grid))
        for j in range(len(grid[0]))
        if is_land(grid, i, j) and not sink(grid, i, j)
    )
