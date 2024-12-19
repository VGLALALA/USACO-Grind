import sys

# Read input
input = sys.stdin.readline
cube_size, num_queries = map(int, input().split())
operations = []
for _ in range(num_queries):
    operations += list(map(int, input().split()))

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

results = []
i = 0
for _ in range(num_queries):
    x, y, z = operations[i:i+3]
    i += 3
    
    coords = [(y,z,'x'), (x,z,'y'), (x,y,'z')]
    for i, j, dim in coords:
        holes_per_line[dim][i][j] += 1
        if holes_per_line[dim][i][j] == cube_size and not completed_lines[dim][i][j]:
            completed_lines[dim][i][j] = True
            line_counts[dim] += 1
    
    total = sum(line_counts.values())
    results.append(total)

for r in results:
    print(r)
