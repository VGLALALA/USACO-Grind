from sys import stdin, stdout

def calculate_groups(index_list, max_distance):
    group_count = 1
    last_position = index_list[0]
    for position in index_list[1:]:
        if position - last_position > max_distance:
            group_count += 1
            last_position = position
    return group_count

def process_label(index_list, group_results, total_cows):
    current_distance = total_cows
    while current_distance > 0:
        previous_distance = current_distance
        groups = calculate_groups(index_list, current_distance)

        low, high = 1, current_distance
        while low <= high:
            mid = (low + high) // 2
            if calculate_groups(index_list, mid) == groups:
                previous_distance = mid
                high = mid - 1
            else:
                low = mid + 1

        group_results[previous_distance] += groups
        group_results[current_distance + 1] -= groups

        current_distance = previous_distance - 1

def thing():
    max_cows = int(1.01e6)
    total_cows = int(stdin.readline())
    cow_labels = [0] + list(map(int, stdin.readline().split()))
    group_results = [0] * (total_cows + 2)
    cow_positions = [[] for _ in range(max_cows)]

    for cow_index in range(1, total_cows + 1):
        cow_positions[cow_labels[cow_index]].append(cow_index)

    for positions in cow_positions:
        if positions:
            process_label(positions, group_results, total_cows)

    current_groups = 0
    for i in range(1, total_cows + 1):
        current_groups += group_results[i]
        stdout.write(f"{current_groups}\n")

thing()