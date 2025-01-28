def that():
    grid_size, num_days = map(int, input().split())
    conveyor_grid = [[0] * grid_size for _ in range(grid_size)]
    conveyor_updates = []

    for _ in range(num_days):
        row, col, direction = input().split()
        row, col = int(row) - 1, int(col) - 1
        conveyor_grid[row][col] = direction
        conveyor_updates.append((row, col, direction))

    min_unusable_cells = [0] * num_days
    remaining_unusable = grid_size * grid_size
    visited_cells = [[0] * grid_size for _ in range(grid_size)]

    bfs_queue = []

    for i in range(grid_size):
        for j in range(grid_size):
            if i == 0 or j == 0 or i == grid_size - 1 or j == grid_size - 1:
                if conveyor_grid[i][j] == 0:
                    visited_cells[i][j] = 1
                    bfs_queue.append((i, j))
                    remaining_unusable -= 1
                if i == 0 and conveyor_grid[i][j] == 'U' and not visited_cells[i][j]:
                    visited_cells[i][j] = 1
                    bfs_queue.append((i, j))
                    remaining_unusable -= 1
                if j == 0 and conveyor_grid[i][j] == 'L' and not visited_cells[i][j]:
                    visited_cells[i][j] = 1
                    bfs_queue.append((i, j))
                    remaining_unusable -= 1
                if i == grid_size - 1 and conveyor_grid[i][j] == 'D' and not visited_cells[i][j]:
                    visited_cells[i][j] = 1
                    bfs_queue.append((i, j))
                    remaining_unusable -= 1
                if j == grid_size - 1 and conveyor_grid[i][j] == 'R' and not visited_cells[i][j]:
                    visited_cells[i][j] = 1
                    bfs_queue.append((i, j))
                    remaining_unusable -= 1

    while bfs_queue:
        r, c = bfs_queue.pop(0)

        if r - 1 >= 0 and (conveyor_grid[r - 1][c] == 'D' or conveyor_grid[r - 1][c] == 0) and not visited_cells[r - 1][c]:
            visited_cells[r - 1][c] = 1
            bfs_queue.append((r - 1, c))
            remaining_unusable -= 1
        if r + 1 < grid_size and (conveyor_grid[r + 1][c] == 'U' or conveyor_grid[r + 1][c] == 0) and not visited_cells[r + 1][c]:
            visited_cells[r + 1][c] = 1
            bfs_queue.append((r + 1, c))
            remaining_unusable -= 1
        if c - 1 >= 0 and (conveyor_grid[r][c - 1] == 'R' or conveyor_grid[r][c - 1] == 0) and not visited_cells[r][c - 1]:
            visited_cells[r][c - 1] = 1
            bfs_queue.append((r, c - 1))
            remaining_unusable -= 1
        if c + 1 < grid_size and (conveyor_grid[r][c + 1] == 'L' or conveyor_grid[r][c + 1] == 0) and not visited_cells[r][c + 1]:
            visited_cells[r][c + 1] = 1
            bfs_queue.append((r, c + 1))
            remaining_unusable -= 1

    min_unusable_cells[num_days - 1] = remaining_unusable

    for day in range(num_days - 2, -1, -1):
        row, col, direction = conveyor_updates[day + 1]

        conveyor_grid[row][col] = 0

        start_new_bfs = False

        if row == 0 and not visited_cells[row][col] and conveyor_grid[row][col] != 'U':
            visited_cells[row][col] = 1
            bfs_queue.append((row, col))
            remaining_unusable -= 1
            start_new_bfs = True
        elif col == 0 and not visited_cells[row][col] and conveyor_grid[row][col] != 'L':
            visited_cells[row][col] = 1
            bfs_queue.append((row, col))
            remaining_unusable -= 1
            start_new_bfs = True
        elif row == grid_size - 1 and not visited_cells[row][col] and conveyor_grid[row][col] != 'D':
            visited_cells[row][col] = 1
            bfs_queue.append((row, col))
            remaining_unusable -= 1
            start_new_bfs = True
        elif col == grid_size - 1 and not visited_cells[row][col] and conveyor_grid[row][col] != 'R':
            visited_cells[row][col] = 1
            bfs_queue.append((row, col))
            remaining_unusable -= 1
            start_new_bfs = True

        if not visited_cells[row][col]:
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = row + dr, col + dc
                if 0 <= nr < grid_size and 0 <= nc < grid_size:
                    if visited_cells[nr][nc] and not visited_cells[row][col]:
                        visited_cells[row][col] = 1
                        bfs_queue.append((row, col))
                        remaining_unusable -= 1
                        start_new_bfs = True
                        break

        while bfs_queue:
            r, c = bfs_queue.pop(0)

            if r - 1 >= 0 and (conveyor_grid[r - 1][c] == 'D' or conveyor_grid[r - 1][c] == 0) and not visited_cells[r - 1][c]:
                visited_cells[r - 1][c] = 1
                bfs_queue.append((r - 1, c))
                remaining_unusable -= 1
            if r + 1 < grid_size and (conveyor_grid[r + 1][c] == 'U' or conveyor_grid[r + 1][c] == 0) and not visited_cells[r + 1][c]:
                visited_cells[r + 1][c] = 1
                bfs_queue.append((r + 1, c))
                remaining_unusable -= 1
            if c - 1 >= 0 and (conveyor_grid[r][c - 1] == 'R' or conveyor_grid[r][c - 1] == 0) and not visited_cells[r][c - 1]:
                visited_cells[r][c - 1] = 1
                bfs_queue.append((r, c - 1))
                remaining_unusable -= 1
            if c + 1 < grid_size and (conveyor_grid[r][c + 1] == 'L' or conveyor_grid[r][c + 1] == 0) and not visited_cells[r][c + 1]:
                visited_cells[r][c + 1] = 1
                bfs_queue.append((r, c + 1))
                remaining_unusable -= 1

        min_unusable_cells[day] = remaining_unusable

    print('\n'.join(map(str, min_unusable_cells)))

that()