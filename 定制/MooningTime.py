import sys

def is_valid_brick(pattern):
    return len(pattern) == 3 and pattern[0] != pattern[1] and pattern[1] == pattern[2]

def get_updated_substring(cheese_block, carved_position, new_char, start, block_size):
    if start < 0 or start + 2 >= block_size:
        return None
    if start <= carved_position < start + 3:
        return cheese_block[start:carved_position] + new_char + cheese_block[carved_position + 1:start + 3]
    return cheese_block[start:start + 3]

def count_brick_patterns(cheese_block, block_size):
    pattern_count = {}
    for position in range(block_size - 2):
        current_pattern = cheese_block[position:position + 3]
        if is_valid_brick(current_pattern):
            pattern_count[current_pattern] = pattern_count.get(current_pattern, 0) + 1
    return pattern_count

def find_valid_brick_patterns(pattern_count, threshold):
    valid_bricks = set()
    for brick_pattern, frequency in pattern_count.items():
        if frequency >= threshold:
            valid_bricks.add(brick_pattern)
    return valid_bricks

def evaluate_carved_bricks(cheese_block, block_size, pattern_count, threshold):
    valid_bricks = set()
    possible_chars = "abcdefghijklmnopqrstuvwxyz"
    for carved_position in range(block_size):
        current_char = cheese_block[carved_position]
        for new_char in possible_chars:
            if new_char == current_char:
                continue

            frequency_changes = {}
            impacted_positions = [carved_position - 2, carved_position - 1, carved_position]

            for start in impacted_positions:
                if start < 0 or start + 2 >= block_size:
                    continue

                before_pattern = cheese_block[start:start + 3]
                after_pattern = get_updated_substring(cheese_block, carved_position, new_char, start, block_size)

                if is_valid_brick(before_pattern):
                    frequency_changes[before_pattern] = frequency_changes.get(before_pattern, 0) - 1

                if after_pattern and is_valid_brick(after_pattern):
                    frequency_changes[after_pattern] = frequency_changes.get(after_pattern, 0) + 1

            for pattern in frequency_changes:
                original_frequency = pattern_count.get(pattern, 0)
                updated_frequency = original_frequency + frequency_changes[pattern]
                if updated_frequency >= threshold:
                    valid_bricks.add(pattern)
    return valid_bricks

def that():
    input_data = sys.stdin.read().strip().split()
    block_size, threshold = int(input_data[0]), int(input_data[1])
    cheese_block = input_data[2]

    pattern_count = count_brick_patterns(cheese_block, block_size)
    valid_bricks = find_valid_brick_patterns(pattern_count, threshold)
    valid_bricks.update(evaluate_carved_bricks(cheese_block, block_size, pattern_count, threshold))

    sorted_valid_bricks = sorted(valid_bricks)
    print(len(sorted_valid_bricks))
    print("\n".join(sorted_valid_bricks))

that()
