class Solution:
    def count_islands(self, grid: list) -> int:
        """
        Count the number of islands in a 2D grid.
        Uses depth-first search to mark visited land cells.
        """
        if not grid:
            return 0

        total_rows = len(grid)
        total_columns = len(grid[0])
        island_count = 0

        def mark_island_as_visited(row_index: int, column_index: int) -> None:
            if row_index < 0 or row_index >= total_rows:
                return
            if column_index < 0 or column_index >= total_columns:
                return
            if grid[row_index][column_index] != '1':
                return

            grid[row_index][column_index] = '0'
            mark_island_as_visited(row_index + 1, column_index)
            mark_island_as_visited(row_index - 1, column_index)
            mark_island_as_visited(row_index, column_index + 1)
            mark_island_as_visited(row_index, column_index - 1)

        for row_index in range(total_rows):
            for column_index in range(total_columns):
                if grid[row_index][column_index] == '1':
                    island_count += 1
                    mark_island_as_visited(row_index, column_index)

        return island_count
