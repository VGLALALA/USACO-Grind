from collections import deque

def that():
    grid_size, num_days = map(int, input().split())
    conveyor_grid = [[0] * grid_size for _ in range(grid_size)]
    bfs_queue = deque()
    conveyor_updates = []

    for _ in range(num_days):
        row, col, direction = input().split()
        row, col = int(row) - 1, int(col) - 1
        conveyor_grid[row][col] = direction
        conveyor_updates.append((row, col, direction))

    min_unusable_cells = [0] * num_days
    remaining_unusable = grid_size * grid_size
    visited_cells = [[0] * grid_size for _ in range(grid_size)]

    for i in range(grid_size):
        for j in range(grid_size):
            if i == 0 or j == 0 or i == grid_size - 1 or j == grid_size - 1:
                if conveyor_grid[i][j] == 0:
                    bfs_queue.append((i, j))
                    visited_cells[i][j] = 1
                    remaining_unusable -= 1
                if i == 0 and conveyor_grid[i][j] == 'U':
                    bfs_queue.append((i, j))
                    visited_cells[i][j] = 1
                    remaining_unusable -= 1
                if j == 0 and conveyor_grid[i][j] == 'L':
                    bfs_queue.append((i, j))
                    visited_cells[i][j] = 1
                    remaining_unusable -= 1
                if i == grid_size - 1 and conveyor_grid[i][j] == 'D':
                    bfs_queue.append((i, j))
                    visited_cells[i][j] = 1
                    remaining_unusable -= 1
                if j == grid_size - 1 and conveyor_grid[i][j] == 'R':
                    bfs_queue.append((i, j))
                    visited_cells[i][j] = 1
                    remaining_unusable -= 1

    while bfs_queue:
        row, col = bfs_queue.popleft()

        if row - 1 >= 0 and (conveyor_grid[row - 1][col] == 'D' or conveyor_grid[row - 1][col] == 0) and not visited_cells[row - 1][col]:
            visited_cells[row - 1][col] = 1
            bfs_queue.appendleft((row - 1, col))
            remaining_unusable -= 1
        if row + 1 < grid_size and (conveyor_grid[row + 1][col] == 'U' or conveyor_grid[row + 1][col] == 0) and not visited_cells[row + 1][col]:
            visited_cells[row + 1][col] = 1
            bfs_queue.appendleft((row + 1, col))
            remaining_unusable -= 1
        if col - 1 >= 0 and (conveyor_grid[row][col - 1] == 'R' or conveyor_grid[row][col - 1] == 0) and not visited_cells[row][col - 1]:
            visited_cells[row][col - 1] = 1
            bfs_queue.appendleft((row, col - 1))
            remaining_unusable -= 1
        if col + 1 < grid_size and (conveyor_grid[row][col + 1] == 'L' or conveyor_grid[row][col + 1] == 0) and not visited_cells[row][col + 1]:
            visited_cells[row][col + 1] = 1
            bfs_queue.appendleft((row, col + 1))
            remaining_unusable -= 1

    min_unusable_cells[num_days - 1] = remaining_unusable

    for day in range(num_days - 2, -1, -1):
        row, col, direction = conveyor_updates[day + 1]
        if row == 0 and conveyor_grid[row][col] != 'U' and not visited_cells[row][col]:
            bfs_queue.append((row, col))
            visited_cells[row][col] = 1
            remaining_unusable -= 1
        elif col == 0 and conveyor_grid[row][col] != 'L' and not visited_cells[row][col]:
            bfs_queue.append((row, col))
            visited_cells[row][col] = 1
            remaining_unusable -= 1
        elif row == grid_size - 1 and conveyor_grid[row][col] != 'D' and not visited_cells[row][col]:
            bfs_queue.append((row, col))
            visited_cells[row][col] = 1
            remaining_unusable -= 1
        elif col == grid_size - 1 and conveyor_grid[row][col] != 'R' and not visited_cells[row][col]:
            bfs_queue.append((row, col))
            visited_cells[row][col] = 1
            remaining_unusable -= 1

        if not visited_cells[row][col]:
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                new_row, new_col = row + dr, col + dc
                if 0 <= new_row < grid_size and 0 <= new_col < grid_size and not visited_cells[row][col] and visited_cells[new_row][new_col]:
                    bfs_queue.append((row, col))
                    visited_cells[row][col] = 1
                    remaining_unusable -= 1

        conveyor_grid[row][col] = 0

        while bfs_queue:
            row, col = bfs_queue.popleft()

            if row - 1 >= 0 and (conveyor_grid[row - 1][col] == 'D' or conveyor_grid[row - 1][col] == 0) and not visited_cells[row - 1][col]:
                visited_cells[row - 1][col] = 1
                bfs_queue.appendleft((row - 1, col))
                remaining_unusable -= 1
            if row + 1 < grid_size and (conveyor_grid[row + 1][col] == 'U' or conveyor_grid[row + 1][col] == 0) and not visited_cells[row + 1][col]:
                visited_cells[row + 1][col] = 1
                bfs_queue.appendleft((row + 1, col))
                remaining_unusable -= 1
            if col - 1 >= 0 and (conveyor_grid[row][col - 1] == 'R' or conveyor_grid[row][col - 1] == 0) and not visited_cells[row][col - 1]:
                visited_cells[row][col - 1] = 1
                bfs_queue.appendleft((row, col - 1))
                remaining_unusable -= 1
            if col + 1 < grid_size and (conveyor_grid[row][col + 1] == 'L' or conveyor_grid[row][col + 1] == 0) and not visited_cells[row][col + 1]:
                visited_cells[row][col + 1] = 1
                bfs_queue.appendleft((row, col + 1))
                remaining_unusable -= 1

        min_unusable_cells[day] = remaining_unusable

    print('\n'.join(map(str, min_unusable_cells)))

that()
