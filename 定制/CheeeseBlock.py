import sys

def process_query(cube_x, cube_y, cube_z, block_counts, completed_planes, plane_totals, cube_size):
    coordinates = [(cube_y, cube_z, 'x'), (cube_x, cube_z, 'y'), (cube_x, cube_y, 'z')]
    for i, j, plane in coordinates:
        block_counts[plane][i][j] += 1
        if block_counts[plane][i][j] == cube_size and not completed_planes[plane][i][j]:
            completed_planes[plane][i][j] = True
            plane_totals[plane] += 1
    return sum(plane_totals.values())

def that():
    input = sys.stdin.readline
    cube_size, query_count = map(int, input().split())
    carve_operations = []
    for _ in range(query_count):
        carve_operations += list(map(int, input().split()))

    block_counts = {
        'x': [[0] * cube_size for _ in range(cube_size)],
        'y': [[0] * cube_size for _ in range(cube_size)], 
        'z': [[0] * cube_size for _ in range(cube_size)]
    }

    completed_planes = {
        'x': [[False] * cube_size for _ in range(cube_size)],
        'y': [[False] * cube_size for _ in range(cube_size)],
        'z': [[False] * cube_size for _ in range(cube_size)]
    }

    plane_totals = {'x': 0, 'y': 0, 'z': 0}

    output_results = []
    operation_index = 0
    for _ in range(query_count):
        cube_x, cube_y, cube_z = carve_operations[operation_index:operation_index+3]
        operation_index += 3
        total_planes = process_query(cube_x, cube_y, cube_z, block_counts, completed_planes, plane_totals, cube_size)
        output_results.append(total_planes)

    for result in output_results:
        print(result)

that()
