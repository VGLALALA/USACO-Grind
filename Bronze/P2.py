import sys

# Read input
raw_input = sys.stdin.read().strip().split()
cube_size, num_queries = map(int, raw_input[0:2])
operations = list(map(int, raw_input[2:]))

# Initialize tracking arrays for each dimension
holes_per_line = {
    'x': [[0]*cube_size for _ in range(cube_size)],
    'y': [[0]*cube_size for _ in range(cube_size)], 
    'z': [[0]*cube_size for _ in range(cube_size)]
}

completed_lines = {
    'x': [[False]*cube_size for _ in range(cube_size)],
    'y': [[False]*cube_size for _ in range(cube_size)],
    'z': [[False]*cube_size for _ in range(cube_size)]
}

line_counts = {'x': 0, 'y': 0, 'z': 0}

# Process queries
results = []
op_idx = 0
for _ in range(num_queries):
    x, y, z = operations[op_idx:op_idx+3]
    op_idx += 3
    
    # Check each dimension
    coords = [(y,z,'x'), (x,z,'y'), (x,y,'z')]
    for i, j, dim in coords:
        holes_per_line[dim][i][j] += 1
        if holes_per_line[dim][i][j] == cube_size and not completed_lines[dim][i][j]:
            completed_lines[dim][i][j] = True
            line_counts[dim] += 1
    
    total = sum(line_counts.values())
    results.append(str(total))

print('\n'.join(results))
